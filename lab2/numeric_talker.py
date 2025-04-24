import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Int8   # ← import the 8-bit integer type

class NumericTalker(Node):

    def __init__(self):
        super().__init__('numeric_talker')

        # publisher #1: String on /chatter (unchanged)
        self.string_pub = self.create_publisher(String, 'chatter', 10)

        # publisher #2: Int8 on /numeric_chatter
        self.numeric_pub = self.create_publisher(Int8, 'numeric_chatter', 10)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.counter = 0

    def timer_callback(self):
        # --- String message (as before) ---
        str_msg = String()
        str_msg.data = f'Hello World, {self.counter}'
        self.string_pub.publish(str_msg)
        self.get_logger().info(f'Publishing string: "{str_msg.data}"')

        # --- Numeric message ---
        num_msg = Int8()
        num_msg.data = self.counter
        self.numeric_pub.publish(num_msg)
        self.get_logger().info(f'Publishing numeric: {num_msg.data}')

        # increment & wrap around at 127 → 0
        self.counter = (self.counter + 1) % 128

def main(args=None):
    rclpy.init(args=args)
    node = NumericTalker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
