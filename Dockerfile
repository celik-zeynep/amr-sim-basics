FROM ros:humble-ros-base

WORKDIR /ros2_ws

RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    git \
    ros-humble-turtlebot3-gazebo \
    ros-humble-turtlebot3-teleop \
    && rm -rf /var/lib/apt/lists/*

COPY src /ros2_ws/src

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "export TURTLEBOT3_MODEL=waffle" >> ~/.bashrc

CMD ["bash"]
