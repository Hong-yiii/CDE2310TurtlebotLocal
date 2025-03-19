#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import board
import busio
import adafruit_amg88xx
from std_msgs.msg import Float32MultiArray

class AMG8833Publisher(Node):
    def __init__(self):
        super().__init__('amg8833_publisher')
        
       
        self.publisher_ = self.create_publisher(Float32MultiArray, 'temperature_sensor', 10)
        
        
        self.timer = self.create_timer(1.0, self.publish_data)

        # Initialize I2C and AMG8833 sensor
        i2c_bus = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_amg88xx.AMG88XX(i2c_bus, address=0x69)  # Default I2C address

    def publish_data(self):
        # Read temperature data from sensor
        temp_data = Float32MultiArray()
        temp_data.data = [temp for row in self.sensor.pixels for temp in row]  # Flatten 8×8 array
        
        self.publisher_.publish(temp_data)
        self.get_logger().info("Published AMG8833 temperature data")

def main(args=None):
    rclpy.init(args=args)
    node = AMG8833Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
