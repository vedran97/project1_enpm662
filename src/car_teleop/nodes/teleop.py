#!/usr/bin/python3
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

msg = """
Control Your Car!
---------------------------
    w
a   s   d
a:turn left by 0.1 radians steering angle
d:turn right by 0.1 radians steering angle
w:go forward by 0.5 rad/sec angular velocity of rear wheels
s:go forward by 0.5 rad/sec angular veclocity of rear wheels
space_bar: stop completely
CTRL-C to quit
"""
e = """
Communications Failed
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('custom_teleop')

    pub_right_steering = rospy.Publisher('/robot_urdf/j_support_right_controller/command', Float64, queue_size=10)
    pub_left_steering = rospy.Publisher('/robot_urdf/j_support_left_controller/command', Float64, queue_size=10)
    pub_left_move = rospy.Publisher('/robot_urdf/j_rear_left_wheel_controller/command', Float64, queue_size=10) 
    pub_right_move = rospy.Publisher('/robot_urdf/j_rear_right_wheel_controller/command', Float64, queue_size=10)

    steering_command = 0
    linear_command = 0
    try:
        print(msg)
        while(1):
            key = getKey()
            if key == 'w':
                linear_command-=0.5
                pub_right_move.publish(linear_command)
                pub_left_move.publish(linear_command)
                pub_right_steering.publish(steering_command)
                pub_left_steering.publish(steering_command)
            if key == 's':
                linear_command+=0.5
                pub_right_move.publish(linear_command)
                pub_left_move.publish(linear_command)
                pub_right_steering.publish(steering_command)
                pub_left_steering.publish(steering_command)
            if key == 'a':
                steering_command+=0.1
                pub_right_steering.publish(steering_command)
                pub_left_steering.publish(steering_command)
            elif key == 'd':
                steering_command-=0.1
                pub_right_steering.publish(steering_command)
                pub_left_steering.publish(steering_command)
            elif key == ' ':
                linear_command = 0
                steering_command = 0
                pub_right_move.publish(linear_command)
                pub_left_move.publish(linear_command)
                pub_right_steering.publish(steering_command)
                pub_left_steering.publish(steering_command)
            elif (key == '\x03'):
                    break
            if key in ['w','a','s','d',' ']:
                print("current linear velocity:",linear_command)
                print("steering angle:",steering_command)


    except:
        print(e)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)