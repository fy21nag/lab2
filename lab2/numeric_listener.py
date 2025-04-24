import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int8   # ← import the numeric type

class NumericListener(Node):

    def __init__(self):
        super().__init__('numeric_listener')

        # existing string subscription
        self.string_sub = self.create_subscription(
            String,
            'chatter',
            self.chatter_callback,
            10
        )
        # new numeric subscription
        self.numeric_sub = self.create_subscription(
            Int8,
            'numeric_chatter',
            self.numeric_callback,
            10
        )

    def chatter_callback(self, msg):
        self.get_logger().info(f"I heard string: {msg.data!r}")

    def numeric_callback(self, msg):
        self.get_logger().info(f"I heard number: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = NumericListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
