from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_robot_pkg',
            executable='talker',
            name='custom_talker',
            parameters=[
                {'publish_period': 0.5}  # Periyodu 0.5 saniyeye düşürdük
            ]
        )
    ])
