# Project 1: Mobile Robot in Simulation (TurtleBot3, ROS 2 Humble)

Status values: **Planned**, **In progress**, **Done**.
A requirement is marked Done only after its verification has actually passed.

| ID | Requirement | Verification | Status |
|----|-------------|--------------|--------|
| R1 | A C++ node written by me drives TurtleBot3 forward through the `/cmd_vel` topic. | In Gazebo, the robot moves at least 1 m. | Planned |
| R2 | The TF tree is complete and visible in RViz. | `ros2 run tf2_tools view_frames` shows no disconnected frames. | Planned |
| R3 | The package builds in a clean environment. | GitHub Actions: `colcon build` succeeds with at least 1 package. | Done |
| R4 | Automated checks run in CI. | GitHub Actions: a `colcon test` step passes. | Planned |
