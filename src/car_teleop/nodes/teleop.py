#!/usr/bin/python3
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

msg = """
Control Your Car!
---------------------------
    w
a   s   d
a:turn left by 0.1 radians
d:turn right by 0.1 radians
w:go forward by 0.1 angular velocity
s:go forward by 0.1 angular velocity
space_bar: stop completely
CTRL-C to quit
"""
e = """
Communications Failed
"""

moveBindings = {
        'i':(1,0),
        'o':(1,-1),
        'j':(0,1),
        'l':(0,-1),
        'u':(1,1),
        ',':(-1,0),
        '.':(-1,1),
        'm':(-1,-1),
           }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
          }

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 8
turn = 0.5

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('custom_teleop')

    pub_right = rospy.Publisher('/robot_urdf/j_support_right_controller/command', Float64, queue_size=10)
    pub_left = rospy.Publisher('/robot_urdf/j_support_left_controller/command', Float64, queue_size=10)
    pub_move_left = rospy.Publisher('/robot_urdf/j_rear_left_wheel_controller/command', Float64, queue_size=10) 
    pub_move_right = rospy.Publisher('/robot_urdf/j_rear_right_wheel_controller/command', Float64, queue_size=10)
    x = 0
    th = 0
    status = 0
    count = 0
    acc = 0.1
    target_speed = 0
    target_turn = 0
    control_speed = 0
    control_turn = 0
    steering_command = 0
    linear_command = 0
    try:
        print(msg)
        while(1):
            key = getKey()
            if key == 'w':
                linear_command-=0.05
                pub_move_right.publish(linear_command)
                pub_move_left.publish(linear_command)
            if key == 's':
                linear_command+=0.05
                pub_move_right.publish(linear_command)
                pub_move_left.publish(linear_command)
            if key == 'a':
                steering_command+=0.1
                pub_right.publish(steering_command)
                pub_left.publish(steering_command)
            elif key == 'd':
                steering_command-=0.1
                pub_right.publish(steering_command)
                pub_left.publish(steering_command)
            elif key == ' ':
                linear_command = 0
                steering_command = 0
                pub_move_right.publish(linear_command)
                pub_move_left.publish(linear_command)
                pub_right.publish(steering_command)
                pub_left.publish(steering_command)
            elif (key == '\x03'):
                    break
            if key in ['w','a','s','d']:
                print("current linear velocity:",linear_command)
                print("steering angle:",steering_command)


    except:
        print(e)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)