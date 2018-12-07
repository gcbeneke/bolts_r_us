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
Q1 = [0.31180,1.00045,-0.14235,0,0.72213,0.17294]
Q5 = [-1.57,0,0,0,0,0]
Q2 = [1.5,0,-1.57,0,0,0]
Q3 = [1.5,-0.2,-1.57,0,0,0]
Q4 = [0,0,0,0,0,0]
positiePlaat = [0.11386,1.09483,0.30491,-2.21224,1.47092,0.12776]
homePosition = [0,0,0,0,0,0]

## Alle jointsstates voor de eerste positie
refpos1 = [-0.05583, 1.22699, -0.18286,0.78646, -1.20635, -0.52067] # positie 1 (0 punt)
refpos2 = [0.04141, 1.37890, -0.50648, 0.93691,-1.13694,-0.70177] # positie 2
boltPos = [0.52298, 0.82716, 0.16881, 0.02369, 0.52621, -0.42037]
safeBoltPos = [0.52299, 0.63573, 0.15993, 0.01783, 0.72653, -0.41322]
afstandtotj = 6.45 # afstand tussen pos 1 en pos 2
status = 0
movepos = refpos1
movement = [0, 0, 0, 0, 0, 0]
statusRobot = 0
alwaysTrue = True
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
def calibration():
    global joints_pos
    global status
    global statusRobot
    i = 0
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    rospy.Subscriber("bru_ctrl_state", Int8, state_callback)

    try:
            rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
            if status == 3:
            		joint_states = rospy.wait_for_message("joint_states", JointState)
            		joints_pos = joint_states.position
            		movepos = joints_pos

            		g.trajectory.points = [
            	   	    	JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
            	    	   	JointTrajectoryPoint(positions=homePosition, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0))]

            	    	client.send_goal(g)
                    	client.wait_for_result()
                        joint_states = rospy.wait_for_message("joint_states", JointState)
                        joints_pos = joint_states.position
                        for x in joints_pos:
                            if x < 0.001 and x > -0.001:
                                statusRobot = 1
                                i = i +1
                                print "Joint " , i , " calibrated correctly"
                            else:
                                print "Error while calibrating " , i , " try again"


    except KeyboardInterrupt:
            client.cancel_goal()
            raise
    except:
        	raise

def moveToWarehouse(x):
    global movement
    global statusRobot
    x = 0
    temp = 0
    ready = False
    global movepos
    global joints_pos
    global status
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
    if status == 1:
        start = True
        stop = False
    elif status == 2:
        stop = True
        start = False
    elif status == 3:
        stop = False
        start = False
    else:
        start = False
        stop = False
    try:
        if start == True:
            for x in range(1):
                rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
                if status == 1:
            		joint_states = rospy.wait_for_message("joint_states", JointState)
            		joints_pos = joint_states.position
            		movepos = joints_pos
            		x = temp + 1
            		movement = calculateToPosition(movepos, boltPos)
            		movepos = movement
            		g.trajectory.points = [
            	   	    	JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
            	    	   	JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0))]

            	    	client.send_goal(g)
                    	client.wait_for_result()
                joint_states = rospy.wait_for_message("joint_states", JointState)
                joints_pos = joint_states.position
                offset = calculateOffSet(joints_pos, movepos)
                i = 0
                for x in offset:
                    if x < 0.001 and x > -0.001:
                        i = i + 1
                    if i > 5:
                        print ""
                        print "--------------------"
                        print "Arrived at warehouse position"
                        statusRobot = 3
    except KeyboardInterrupt:
		client.cancel_goal()
		raise
    except:
    	raise

def moveAboveBolt():
    global movement
    global statusRobot
    x = 0
    temp = 0
    ready = False
    global movepos
    global joints_pos
    global status
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
    if status == 1:
        start = True
        stop = False
    elif status == 2:
        stop = True
        start = False
    elif status == 3:
        stop = False
        start = False
    else:
        start = False
        stop = False
    try:
        if start == True:
            print temp
            for x in range(1):
                rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
                if status == 1:
            		joint_states = rospy.wait_for_message("joint_states", JointState)
            		joints_pos = joint_states.position
            		movepos = joints_pos
            		x = temp + 1
            		movement = calculateToPosition(movepos, safeBoltPos)
            		movepos = movement
            		g.trajectory.points = [
            	   	    	JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
            	    	   	JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0))]

            	    	client.send_goal(g)
                    	client.wait_for_result()
                joint_states = rospy.wait_for_message("joint_states", JointState)
                joints_pos = joint_states.position
                offset = calculateOffSet(joints_pos, movepos)
                i = 0
                for x in offset:
                    if x < 0.001 and x > -0.001:
                        i = i + 1
                    if i > 5:
                        if statusRobot == 1:
                            statusRobot = 2
                        if statusRobot == 4:
                            statusRobot = 5
                        print ""
                        print "--------------------"
                        print "Arrived at safe position"
    except KeyboardInterrupt:
		client.cancel_goal()
		raise
    except:
    	raise

def moveBoltToHole():
    global movement
    global statusRobot
    x = 0
    temp = 0
    ready = False
    global movepos
    global joints_pos
    global status
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
    if status == 1:
        #print "1"
        start = True
        stop = False
    elif status == 2:
        #print "2"
        stop = True
        start = False
    elif status == 3:
        stop = False
        start = False
    else:
        start = False
        stop = False
    try:
        if start == True:
            #print temp
            for x in range(1):
                #print x
                rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
                if status == 1:
            		joint_states = rospy.wait_for_message("joint_states", JointState)
            		joints_pos = joint_states.position
            		movepos = joints_pos
            		x = temp + 1
            		movement = calculateToPosition(movepos, refpos1)
            		movepos = movement
            		#print movement
            		g.trajectory.points = [
            	   	    	JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
            	    	   	JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0))]

            	    	client.send_goal(g)
                    	client.wait_for_result()
                joint_states = rospy.wait_for_message("joint_states", JointState)
                joints_pos = joint_states.position
                offset = calculateOffSet(joints_pos, movepos)
                i = 0
                for x in offset:
                    if x < 0.001 and x > -0.001:
                        i = i + 1
                    if i > 5:
                        statusRobot = 6
                        print ""
                        print "--------------------"
                        print "Arrived at hole position"
    except KeyboardInterrupt:
		client.cancel_goal()
		raise
    except:
    	raise

def main():
    global client
    global statusRobot
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
        print "Connected to ABB IRB120"
        print ""
        print "Choose what to do:"
        print "- Press the calibratebutton to calibrate"
        print "- Press the startbutton to start"
        print "- Press the stopbutton to quit the program"
        parameters = rospy.get_param(None)
        while not rospy.is_shutdown():
            pub.publish(statusRobot)
            rate.sleep()
            if statusRobot == 0:
                #print "Calibrate"
                calibration()
            elif statusRobot == 2:
                moveToWarehouse(x)
            elif statusRobot == 4 or statusRobot == 1:
                #print "Move Bolt"
                moveAboveBolt()
            elif statusRobot == 5:
                moveBoltToHole()
            #print "Iteratie"

            index = str(parameters).find('prefix')
            if (index > 0):
                prefix = str(parameters)[index+len("prefix': '"):(index+len("prefix': '")+str(parameters)[index+len("prefix': '"):-1].find("'"))]
                for i, name in enumerate(JOINT_NAMES):
                    JOINT_NAMES[i] = prefix + name

        rospy.spin()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

if __name__ == '__main__': main()
