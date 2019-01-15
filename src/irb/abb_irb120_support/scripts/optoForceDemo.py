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

rotz = [[-0.7071, -0.7071, 0],
    [0.7071, -0.7071, 0],
    [0, 0 ,1]]

homePos = [0.01897, 0.16661, 0.46416, 0.03350, -0.65015, -0.11888]
wantedPos = [0.01897, 0.16661, 0.46416, 0.03350, -0.65015, -0.11888]

## ophalen knoppenstatus
def robot_state_callback(msg):
    global status
    status = msg.data

## functie voor het bepalen van de gewenste beweging
def robot_currentValues_callback(msg):
    global y
    ##verhouding waarmee wordt berekent hoeveel in de X en Y moet worden bewogen
    verhoudingY = -0.00005
    verhoudingX = -0.00001
    current_value = msg.p

    ## Als diagonaal op de optoforce kracht wordt gemeten
    if (current_value[0] < -2500 or current_value[0] > 2500) and (current_value[1] < -2500 or current_value[1] > 2500) and status == 6:
        standX = verhoudingX * current_value[0]
        standY = verhoudingY * current_value[1]
        y = 3
        correction(standX, standY, y)
    ## Als boven of onder op de optoforce kracht wordt gemeten
    elif (current_value[1] < -2500 or current_value[1] > 2500) and status == 6:
        standY = verhoudingY * current_value[1]
        y = 1
        correction(0, standY, y)
    ## Als links of rechts op de optoforce kracht wordt gemeten
    elif (current_value[0] < -3000 or current_value[0] > 3000) and status == 6:
        standX = verhoudingX * current_value[0]
        y = 2
        correction(standX, 0, y)

## functie voor het reageren op de krachten
def correction(standX, standY, intval):
    global wantedPos
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES

    ## tuple omzetten naar list
    wantedPos = list(wantedPos)

    ## controleren welke correctie uitgevoerd moet worden
    if intval == 1:
        wantedPos[4] += standY
    elif intval == 2:
        wantedPos[0] -= standX
    elif intval == 3:
        wantedPos[0] -= standX
        wantedPos[4] += standY
    wantedPos = tuple(wantedPos)

    print wantedPos

    ## huidige positie opvragen
    joint_states = rospy.wait_for_message("joint_states", JointState)
    joints_pos = joint_states.position

    ## bewegen naar gecorigeerde positie
    g.trajectory.points = [
            JointTrajectoryPoint(positions=joints_pos, velocities=[0], accelerations=[0], effort = [0],  time_from_start=rospy.Duration(0.0)),
            JointTrajectoryPoint(positions=wantedPos, velocities=[10]*10, accelerations=[5]*10, effort = [0], time_from_start=rospy.Duration(0.001))]

    client.send_goal(g)
    client.wait_for_result()


def main():
    global client
    global status
    global wantedPos
    try:
        ## initialisatie en aanmaken van subscribers
        rospy.init_node("moveRobot", anonymous=True, disable_signals=True)
        rospy.Subscriber("bru_opt_optoforce", Int8, robot_state_callback)
        rospy.Subscriber("bru_opt_force_calculation", Forces, robot_currentValues_callback, queue_size=1)
        client = actionlib.SimpleActionClient('joint_trajectory_action', FollowJointTrajectoryAction)
        client.wait_for_server()
        parameters = rospy.get_param(None)

        ## huidige joint positie opvragen
        joint_states = rospy.wait_for_message("joint_states", JointState)
        joints_pos = joint_states.position
        wantedPos = joints_pos
        ## Programma dat wordt uitgevoerd
        while not rospy.is_shutdown():
            i = 0
        rospy.spin()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

if __name__ == '__main__': main()
