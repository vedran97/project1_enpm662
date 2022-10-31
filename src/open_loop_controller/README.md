# Purpose and usage:

1. This package generates a trajectory and commands, to move a robot (defined under robot_urdf package) in a straight line for a finite time
2. This package has 2 launch files, which executes the controller command publisher and controller command subscriber nodes.
3. Post building the project, in another terminal call "roslaunch open_loop_controller command_publisher.launch" for publishing controller commands.
4. For subscribing to them, open another terminal window and run "roslaunch open_loop_controller command_subscriber.launch"
5. Before launching these nodes, you have to first spawn the robot in a world, for further instructions pls refer robot_urdf package's readme