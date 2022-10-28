#include <iostream>
#include "ros/ros.h"
#include "std_msgs/Float64.h"

void steeringCommandCallback(const std_msgs::Float64::ConstPtr& msg)
{
  ROS_INFO("steering command: [%f]", msg->data);
}
void driveCommandCallback(const std_msgs::Float64::ConstPtr& msg)
{
  ROS_INFO("drive command: [%f]", msg->data);
}


int main(int argc, char **argv)
{
 
  ros::init(argc, argv, "/controller_command_subscriber");

  ros::NodeHandle n;

  ros::Subscriber steeringCommandSubscriber = n.subscribe("/robot_urdf/j_support_right_controller/command", 100, steeringCommandCallback);
  ros::Subscriber driveCommandSubscriber = n.subscribe("/robot_urdf/j_rear_left_wheel_controller/command", 100, driveCommandCallback);

  ros::spin();

  return 0;
}