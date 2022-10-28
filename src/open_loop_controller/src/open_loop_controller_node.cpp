#include <cstdlib>
#include <iostream>
#include <cmath> 
#include "ros/ros.h"

#include "std_msgs/Float64.h"
std_msgs::Float64 linearVelocityCommand;
std_msgs::Float64 steeringAngleCommand;
/**
 * Assuming 1D motion in X direction
 * Using a velocity profile which is a inverted parabola
 * T is the total time required for a motion to start and finish
 * vmax = max linear velocity
 * v(t) = t*(4*vmax/T)-(4*vmax/(T^2))t^2
 * x(0) = xInitial, x(T) = xFinal where x(t) is x coordinate's positon wrt to time
 * T = (6/4*vmax) * (xFinal - xInitial) //solving integralv(t)dt and adding boundary conditions , we get this
 */
static const constexpr double vmax = 0.5; // Setting Max linear velocity to (m/s)

double getLinearVelocity(const double& t,const double& T){
    return  t*(4*vmax/T)+(-(4*vmax/(T*T))*t*t);
}
double getT(const double&  xInitial, const double& xFinal){
    return (6/(4*vmax))*(xFinal - xInitial);
}
static const constexpr double radiusOfWheel = 0.2032/2; //Radius o wheel in meters
double getAngularVelocityOfWheel(const double& v){
    return v/radiusOfWheel;
}



int main(int argc, char **argv) {
 
    // Initiate ROS
    ros::init(argc, argv, "open_loop_controller");

    /**
     * Setup ROS nodes 
     */
    ros::NodeHandle node;
;
    ros::Publisher rightSteeringController =
    node.advertise<std_msgs::Float64>("/robot_urdf/j_support_right_controller/command", 10);

    ros::Publisher leftSteeringController =
    node.advertise<std_msgs::Float64>("/robot_urdf/j_support_left_controller/command", 10);

    ros::Publisher rearRightWheel =
    node.advertise<std_msgs::Float64>("/robot_urdf/j_rear_left_wheel_controller/command", 10);

    ros::Publisher rearLeftWheel =
    node.advertise<std_msgs::Float64>("/robot_urdf/j_rear_right_wheel_controller/command", 10);

    const double loopRate = 500; //500 times a second

    ros::Rate loop_rate(loopRate); 

    std_msgs::Float64 angularVelocityCommand;
    std_msgs::Float64 steeringAngleCommand;

    steeringAngleCommand.data = 0;

    double time = 0.0; // seconds (could use stl time literals as units)
    const double timeIncrement = 1/loopRate;
    const double xInit = 0;  
    const double xFinal = 5;
    const double totalTime = getT(xInit,xFinal);

    std::cout<<"total time:"<<totalTime<<std::endl;

    while (ros::ok()) {
        
        ros::spinOnce();

        angularVelocityCommand.data = -getAngularVelocityOfWheel(getLinearVelocity(time,totalTime));

        rearLeftWheel.publish(angularVelocityCommand);
        rearRightWheel.publish(angularVelocityCommand);

        rightSteeringController.publish(steeringAngleCommand);
        leftSteeringController.publish(steeringAngleCommand);

        loop_rate.sleep();

        time += timeIncrement;

        if(time>=totalTime){

            angularVelocityCommand.data = 0;

            rearLeftWheel.publish(angularVelocityCommand);
            rearRightWheel.publish(angularVelocityCommand);

            rightSteeringController.publish(steeringAngleCommand);
            leftSteeringController.publish(steeringAngleCommand);

            ros::spinOnce();
            break;
        }
    }
    std::cout<<"Open loop controller action over, exiting program"<<std::endl;
return 0;
}