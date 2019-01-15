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
from opt.msg import *

status = 0
robotState = 0
avg_value = [0,0,0,0,0,0]
current_value = [0,0,0,0,0,0]

## Ophalen van knoppenstatus
def state_callback(msg):
 	global status
	status = msg.data
 	if status == 2:
 	 	client.cancel_all_goals()
 	 	print "Stop received, stopping robot"
 	 	status = 5


## Ophalen van average offset krachten waarde
def robot_offset_callback(msg):
    global avg_value
    avg_value[0] = msg.offSet[0]
    avg_value[1] = msg.offSet[1]
    avg_value[2] = msg.offSet[2]
    avg_value[3] = msg.offSet[3]
    avg_value[4] = msg.offSet[4]
    avg_value[5] = msg.offSet[5]

## Ophalen van huidige krachten waarde
def robot_currentValues_callback(msg):
    global current_value
    current_value[0] = msg.fx
    current_value[1] = msg.fy
    current_value[2] = msg.fz
    current_value[3] = msg.tx
    current_value[4] = msg.ty
    current_value[5] = msg.tz
    #if current_value[2] <= -7000: #or current_value[2] >= 6000:
    #    client.cancel_all_goals()

client = None

def main():
    global client
    try:
        ## initialisatie node
        rospy.init_node("stop_robot", anonymous=True, disable_signals=True)
        ## Aanmaken van alle subscribers
        rospy.Subscriber("bru_avg_offset", Corrections, robot_offset_callback)
        rospy.Subscriber("bru_opt_workData", OptoForceData, robot_currentValues_callback)
        rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
        client = actionlib.SimpleActionClient('joint_trajectory_action', FollowJointTrajectoryAction)
        client.wait_for_server()
        while not rospy.is_shutdown():
            i = 0
        rospy.spin()
    except KeyboardInterrupt:
        raise

if __name__ == '__main__': main()
