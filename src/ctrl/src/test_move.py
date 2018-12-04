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

## Alle jointsstates voor de eerste positie
refpos1 = [-0.05583, 1.22699, -0.18286,0.78646, -1.20635, -0.52067] # positie 1 (0 punt)
refpos2 = [0.04141, 1.37890, -0.50648, 0.93691,-1.13694,-0.70177] # positie 2
afstandtotj = 6.45 # afstand tussen pos 1 en pos 2
status = 0
## Ophalen van knoppenstatus
def state_callback(msg):
 	global status
	status = msg.data
	print status
	try:
		# Start knop van de Arduino
			if status == 1:
				#print "Success: "
				movestap()
				return status
		#
			elif status == 2:
				return status
	except rospy.ServiceException, e:
			print "Service call failed: %s"%e

## meerdere posities zodat ie meer linear beweegt
## methode voor het berekenen voor de positie van de joint
def calculatemoment():
    offsetJ = [i - j for i, j in zip(refpos2,refpos1)]
    jRad = [x / afstandtotj for x in offsetJ]
    #jRad = offsetJ /afstandtotj
    beweeg = 0
    bJointtemp = [i * beweeg for i in jRad]
    bJoint = [z+ v for z, v in zip(bJointtemp,refpos1)]
    return bJoint

def calculatemomentstep(bJoint1):
	offsetJ = [i - j for i, j in zip(refpos2,refpos1)]
	jRad = [x / afstandtotj for x in offsetJ]
	    #jRad = offsetJ /afstandtotj
	beweeg = 6
	bJointtemp = [i * beweeg for i in jRad]
	bjointtemp1 = [w / 100 for w in bJointtemp]
	bJoint = [z + v for z, v in zip(bjointtemp1,bJoint1)]
	return bJoint

client = None

def move1():
	movepos = calculatemoment()
	global joints_pos
	g = FollowJointTrajectoryGoal()
	g.trajectory = JointTrajectory()
	g.trajectory.joint_names = JOINT_NAMES
	try:
		joint_states = rospy.wait_for_message("joint_states", JointState)
		joints_pos = joint_states.position
		g.trajectory.points = [
            	JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
            	JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(2.0))]

        	client.send_goal(g)
	        client.wait_for_result()
			#gevraagde positie:

	except KeyboardInterrupt:
	        client.cancel_goal()
	        raise
	except:
	        raise

def movestap():
	movepos = refpos1
	iteratie = 100
	for x in range(100):
		print status
		movepos = calculatemomentstep(movepos)
		global joints_pos
		g = FollowJointTrajectoryGoal()
		g.trajectory = JointTrajectory()
	   	g.trajectory.joint_names = JOINT_NAMES
		try:
			joint_states = rospy.wait_for_message("joint_states", JointState)
			joints_pos = joint_states.position
			g.trajectory.points = [
	            	JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
	            	JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(2.0))]

	        	client.send_goal(g)
		        client.wait_for_result()
				#gevraagde positie:

		except KeyboardInterrupt:
		        client.cancel_goal()
		        raise
		except:
		        raise

def main():
    global client
    try:
        rospy.init_node("test_move", anonymous=True, disable_signals=True)
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
            move1()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

if __name__ == '__main__': main()
