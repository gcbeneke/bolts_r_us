#!/usr/bin/env python
import time
import roslib;
import rospy
import actionlib
import numpy
from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState
from std_msgs.msg import Int8
from math import pi

status = 0
## Ophalen van knoppenstatus
def state_callback(msg):
 	global status
	status = msg.data
        if status == 2:
            client.cancel_all_goals()

client = None

def main():
    global client
    try:
        rospy.init_node("test_move0", anonymous=True, disable_signals=True)
    	rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
        client = actionlib.SimpleActionClient('joint_trajectory_action', FollowJointTrajectoryAction)
        print "Waiting for server..."
        client.wait_for_server()
        print "Connected to server"
        parameters = rospy.get_param(None)
        index = str(parameters).find('prefix')
        if (index > 0):
            prefix = str(parameters)[index+len("prefix': '"):(index+len("prefix': '")+str(parameters)[index+len("prefix': '"):-1].find("'"))]
            for i, name in enumerate(JOINT_NAMES):
                JOINT_NAMES[i] = prefix + name
        inp = raw_input("Continue? y/n: ")[0]
        if (inp == 'y'):
            print "piemel"
    except KeyboardInterrupt:
        raise

if __name__ == '__main__': main()
