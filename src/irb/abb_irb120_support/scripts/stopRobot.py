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
## 
def state_callback(msg):
 	global status
	status = msg.data
	#print status
        if status == 2:
            client.cancel_all_goals()
            print "Stop received, stopping robot"
            status = 5

client = None

def main():
    global client
    try:
        rospy.init_node("stop_robot", anonymous=True, disable_signals=True)
    	rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
        client = actionlib.SimpleActionClient('joint_trajectory_action', FollowJointTrajectoryAction)
        client.wait_for_server()
        parameters = rospy.get_param(None)
        index = str(parameters).find('prefix')
        if (index > 0):
            prefix = str(parameters)[index+len("prefix': '"):(index+len("prefix': '")+str(parameters)[index+len("prefix': '"):-1].find("'"))]
            for i, name in enumerate(JOINT_NAMES):
                JOINT_NAMES[i] = prefix + name
        rospy.spin()
    except KeyboardInterrupt:
        raise

if __name__ == '__main__': main()
