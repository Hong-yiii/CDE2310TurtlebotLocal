import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import board
import time

class TempPublisher(Node):
    def __init__(self):
        super().__init__('flywheel_subscriber')
        self.publisher_ = self.create_publisher(Float32, '/temp', 10)

        timer_period = 1.0  # Publish every 1 second
        self.timer = self.create_timer(timer_period, self.publish_temp)
        self.get_logger().info('Temperature Publisher Started')

    def publish_temp(self):
        try:
            temp_matrix = self.sensor.pixels
            avg_temp = sum([sum(row) for row in temp_matrix]) / 64  # Average of 8x8 matrix
            msg = Float32()
            msg.data = avg_temp
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published temperature: {avg_temp:.2f}°C')
        except Exception as e:
            self.get_logger().error(f"Failed to read from sensor: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = TempPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
