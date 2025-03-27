import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import RPi.GPIO as GPIO

class FlywheelSubscriber(Node):

    def __init__(self):
        super().__init__('flywheel_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # GPIO Setup
        self.ESC_PIN = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ESC_PIN, GPIO.OUT)
        self.pwm = GPIO.PWM(self.ESC_PIN, 50)  # 50Hz for ESC
        self.pwm.start(0)

    def listener_callback(self, msg):
        throttle = msg.data
        if 0 <= throttle <= 2000:
            duty_cycle = 5 + (throttle / 2000) * 5
            self.pwm.ChangeDutyCycle(duty_cycle)
            self.get_logger().info(f'Throttle set to {throttle} µs')
        else:
            self.get_logger().warn('Throttle out of range (0–2000 µs)')

    def destroy_node(self):
        self.pwm.stop()
        GPIO.cleanup()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    flywheel_subscriber = FlywheelSubscriber()

    try:
        rclpy.spin(flywheel_subscriber)
    except KeyboardInterrupt:
        pass

    flywheel_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
