import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher_node')
        
        # Parameter tanımlıyoruz (Varsayılan değer: 1.0 saniye)
        self.declare_parameter('publish_period', 1.0)
        timer_period = self.get_parameter('publish_period').get_parameter_value().double_value
        
        self.publisher_ = self.create_publisher(String, 'robot_status', 10)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Robot devriye geziyor... Adim: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayinlanan Mesaj: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()