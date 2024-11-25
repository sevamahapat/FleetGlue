#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests


class RN1(Node):
    def __init__(self):
        super().__init__('rn1')
        # Publisher to send the mission as a String message
        self.publisher = self.create_publisher(String, 'mission_topic', 10)

        # Timer to poll the REST API every second
        self.timer = self.create_timer(1.0, self.poll_api)

    def poll_api(self):
        try:
            response = requests.get('http://localhost:5000/mission')  # REST API URL
            response.raise_for_status()
            missions = response.json()
            if missions:
                latest_mission = missions[-1]  # Fetch the latest mission
                self.publish_mission(latest_mission['mission'])
        except requests.RequestException as e:
            self.get_logger().error(f"Failed to fetch mission from API: {e}")

    def publish_mission(self, mission):
        # Publish the mission as a String message
        message = String()
        message.data = mission
        self.publisher.publish(message)
        self.get_logger().info(f"Published mission: {mission}")


def main(args=None):
    rclpy.init(args=args)
    node = RN1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
