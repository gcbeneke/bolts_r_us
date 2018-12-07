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

JOINT_NAMES = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
pi = 3.14
homePosition = [0,0,0,0,0,0]
calibrationToCamera = False
## Alle jointsstates voor de eerste positie
status = 0
movement = [0, 0, 0, 0, 0, 0]
statusRobot = 0
alwaysTrue = True
posBottomLeft = [-0.05583, 1.22699, -0.18286,0.78646, -1.20635, -0.52067]
posTopLeft = [-0.05583, 0.99348, -0.08168, 0.82814, -1.11479, -0.62492]
posBottomRight = [0.04141, 1.37890, -0.50648, 0.93691,-1.13694,-0.70177]
## Ophalen van knoppenstatus
def state_callback(msg):
 	global status
	status = msg.data

## Ophalen van robotstatus
def robot_state_callback(data):
    global new_robot_status
    global statusRobot
    new_robot_status = data.data
    statusRobot = new_robot_status

## meerdere posities zodat ie meer linear beweegt
## methode voor het berekenen voor de positie van de joint
def calculateOffSet(currentPos, wantedPos):
    offsetJ = [i - j for i, j in zip(wantedPos,currentPos)]
    return offsetJ

## meerdere posities zodat ie meer linear beweegt
## methode voor het berekenen voor de positie van de joint
def calculateToPosition(currentPos, wantedPos):
	offsetJ = [i - j for i, j in zip(wantedPos,currentPos)]
	updatedCurrentPos = [z + v for z, v in zip(offsetJ,currentPos)]
	return updatedCurrentPos
client = None

## functie om te kalibreren
## beweegt de robot naar de home positie

def calibrationhome():
    global homePosition
    if status == 3:
        calibration(homePosition)
        bottomLeft()

def bottomLeft():
    global posBottomLeft
    print ("Druk op y om naar het 1ste punt te kalibreren")
    inp = raw_input("")[0]
    if inp == 'y':
        position(posBottomLeft)
        bottomright()

def bottomright():
    global posBottomRight
    print ("Druk op y om naar het 2de punt te kalibreren")
    inp = raw_input("")[0]
    if inp == 'y':
        position(posBottomRight)
        topLeft()

def topLeft():
    global posTopLeft
    print ("Druk op y om naar het 3de punt te kalibreren")
    inp = raw_input("")[0]
    if inp == 'y':
        position(posTopLeft)
        homeposition()

def homeposition():
    global homePosition
    global calibrationToCamera
    print ("Druk op y om naar het homepunt te gaan")
    inp = raw_input("")[0]
    if inp == 'y':
        position(homePosition)
        calibrationToCamera = True
        pub = rospy.Publisher("bru_irb_new_robotState", Int8, queue_size=1)
        robotstate = 1
        pub.publish(robotstate)

def position(wantedPos):
    joint_states = rospy.wait_for_message("joint_states", JointState)
    joints_pos = joint_states.position
    movepos = joints_pos
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    g.trajectory.points = [
            JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
            JointTrajectoryPoint(positions=wantedPos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0))]

    client.send_goal(g)
    client.wait_for_result()
    joint_states = rospy.wait_for_message("joint_states", JointState)
    joints_pos = joint_states.position

def calibration(wantedPos):
    global joints_pos
    global status
    global statusRobot
    global alwaysTrue
    global calibrationToCamera
    i = 0
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    rospy.Subscriber("bru_ctrl_state", Int8, state_callback)

    try:
            rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
            if alwaysTrue == True:
            		joint_states = rospy.wait_for_message("joint_states", JointState)
            		joints_pos = joint_states.position
            		movepos = joints_pos

            		g.trajectory.points = [
            	   	    	JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
            	    	   	JointTrajectoryPoint(positions=wantedPos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0))]

            	    	client.send_goal(g)
                    	client.wait_for_result()
                        joint_states = rospy.wait_for_message("joint_states", JointState)
                        joints_pos = joint_states.position
                        for x in joints_pos:
                            if x < 0.001 and x > -0.001:
                                i = i +1
                                print "Joint " , i , " calibrated correctly"
                            else:
                                print "Error while calibrating " , i , " try again"
    except KeyboardInterrupt:
            client.cancel_goal()
            raise
    except:
        	raise

def main():
    global client
    global statusRobot
    global calibrationToCamera

    try:
        x = 0
        counter = 0
        rospy.init_node("moveRobot", anonymous=True, disable_signals=True)
    	rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
        rospy.Subscriber("bru_irb_new_robotState", Int8, robot_state_callback)
        pub = rospy.Publisher('bru_irb_robotState', Int8, queue_size=10)
        rate = rospy.Rate(10)

        client = actionlib.SimpleActionClient('joint_trajectory_action', FollowJointTrajectoryAction)
        client.wait_for_server()
        print ""
        parameters = rospy.get_param(None)
        while calibrationToCamera == False:
            pub.publish(statusRobot)
            rate.sleep()
            if calibrationToCamera == False:
                calibrationhome()

            index = str(parameters).find('prefix')
            if (index > 0):
                prefix = str(parameters)[index+len("prefix': '"):(index+len("prefix': '")+str(parameters)[index+len("prefix': '"):-1].find("'"))]
                for i, name in enumerate(JOINT_NAMES):
                    JOINT_NAMES[i] = prefix + name

    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

if __name__ == '__main__': main()
