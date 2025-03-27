import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import board
import time
from std_msgs.msg import String


class FlywheelSubscriber(Node):

    def __init__(self):
        super().__init__('flywheel_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        #insert more code below
        throttle = msg.data
        if 1000 <= throttle <= 2000:
            duty_cycle = (throttle / 20000) * 100
            self.pwm.ChangeDutyCycle(duty_cycle)
            self.get_logger().info(f'Throttle set to {throttle} µs')
        else:
            self.get_logger().warn('Throttle out of range (1000–2000 µs)')


def main(args=None):
    rclpy.init(args=args)

    flywheel_subscriber = FlywheelSubscriber()

    rclpy.spin(flywheel_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    flywheel_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
