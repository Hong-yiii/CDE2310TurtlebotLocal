import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class PwmCliPublisher(Node):

    def __init__(self):
        super().__init__('pwm_cli_publisher')
        self.publisher_ = self.create_publisher(Int32, 'topic', 10)
        self.get_logger().info("PWM CLI Publisher Started. Enter values (0–2000). Type 'exit' to quit.")
        self.run_cli()

    def run_cli(self):
        try:
            while rclpy.ok():
                user_input = input("Enter PWM (0–2000): ")
                if user_input.lower() == 'exit':
                    break
                try:
                    pwm_value = int(user_input)
                    if 0 <= pwm_value <= 2000:
                        msg = Int32()
                        msg.data = pwm_value
                        self.publisher_.publish(msg)
                        self.get_logger().info(f'Published: {pwm_value}')
                    else:
                        print("Value must be between 0 and 2000.")
                except ValueError:
                    print("Invalid input. Enter an integer between 0 and 2000.")
        except KeyboardInterrupt:
            pass

def main(args=None):
    rclpy.init(args=args)
    node = PwmCliPublisher()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
