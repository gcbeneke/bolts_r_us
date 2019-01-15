#!/usr/bin/env python
import time
import roslib;
import rospy
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState
from std_msgs.msg import Int8
from math import *
from opt.msg import *
from abb_irb120_support.msg import *
import numpy as np

JOINT_NAMES = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']

status = 0
current_value = [0,0,0]

## rotatiematrix
rotz = [[-0.7071, -0.7071, 0],
    [0.7071, -0.7071, 0],
    [0, 0 ,1]]

## berekenen van het nieuwe assenstelsel
def matrixmult (A, B):
    mx = np.matrix(A)
    my = np.matrix(B)

    C = np.matmul(my, mx)
    return C

## publiceert de geroteerde krachten in de vorm van een list
def robot_currentValues_callback(msg):
    pub = rospy.Publisher("bru_opt_force_calculation", Forces, queue_size=1)
    global current_value
    current_value[0] = msg.fx
    current_value[1] = msg.fy
    current_value[2] = msg.fz
    current_value_new = matrixmult(rotz, current_value)
    #print current_value_new
    current_value_new = np.array(current_value_new)[0].tolist()
    pub.publish(current_value_new)

def main():
    try:
        ## initialisatie node en subscribers
        i = 0
        rospy.init_node("forceCalculation", anonymous=True, disable_signals=True)
        rospy.Subscriber("bru_opt_workData", OptoForceData, robot_currentValues_callback, queue_size=1)
        parameters = rospy.get_param(None)
        ## runt zolang rospy runt
        while not rospy.is_shutdown():
            i = i + 1
        rospy.spin()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

if __name__ == '__main__': main()
