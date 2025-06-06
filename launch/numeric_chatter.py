from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lab2',
            executable='numeric_talker',
            name='numeric_talker'
        ),
        Node(
            package='lab2',
            executable='numeric_listener',
            name='numeric_listener'
        ),
    ])
