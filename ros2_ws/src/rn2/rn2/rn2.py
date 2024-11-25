#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RN2(Node):
    def __init__(self):
        super().__init__('rn2')
        # Subscriber to receive the mission as a String message
        self.subscription = self.create_subscription(
            String,
            'mission_topic',
            self.mission_callback,
            10
        )
        self.subscription  # Prevent unused variable warning

    def mission_callback(self, msg):
        # Log the received mission
        self.get_logger().info(f"Received mission: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = RN2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

