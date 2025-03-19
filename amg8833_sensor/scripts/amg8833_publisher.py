#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import numpy as np
import board
import busio
import adafruit_amg88xx
from std_msgs.msg import Float32MultiArray, MultiArrayLayout, MultiArrayDimension

class AMG8833Publisher(Node):
    def __init__(self):
        super().__init__('amg8833_publisher')
        
        # Create a publisher for the sensor data
        self.publisher_ = self.create_publisher(Float32MultiArray, 'temperature_sensor', 10)
        
        # Set up publishing rate (1 Hz)
        self.timer = self.create_timer(1.0, self.publish_data)

        # Initialize I2C and AMG8833 sensor
        i2c_bus = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_amg88xx.AMG88XX(i2c_bus)  # Default I2C address

    def publish_data(self):
        temp_data = Float32MultiArray()
        
        # Convert the sensor data to an 8x8 numpy array
        matrix = np.array(self.sensor.pixels, dtype=np.float32)

        # Assign the 8x8 matrix to the message as a flattened list
        temp_data.data = matrix.flatten().tolist()

        # Define the MultiArray layout to preserve the 8x8 structure
        temp_data.layout = MultiArrayLayout()
        temp_data.layout.dim.append(MultiArrayDimension())
        temp_data.layout.dim.append(MultiArrayDimension())

        temp_data.layout.dim[0].label = "rows"
        temp_data.layout.dim[0].size = 8
        temp_data.layout.dim[0].stride = 64  # Full size of the array (8x8)

        temp_data.layout.dim[1].label = "cols"
        temp_data.layout.dim[1].size = 8
        temp_data.layout.dim[1].stride = 8  # Size of one row

        # Publish the message
        self.publisher_.publish(temp_data)
        self.get_logger().info(f"Published 8x8 AMG8833 temperature data:\n{matrix}")

def main(args=None):
    rclpy.init(args=args)
    node = AMG8833Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

