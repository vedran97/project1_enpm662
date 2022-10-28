# Purpose and usage:

1. This package generates a trajectory and commands, to move a robot (defined under robot_urdf package) in a straight line for a finite time
2. This package has launch file, which executes the open_loop_controller node
3. Post building the project, in another terminal call "roslaunch open_loop_controller open_loop.launch"
4. Before launching this node, you have to first spawn the robot in a world, for further instructions pls refer robot_urdf package's readme