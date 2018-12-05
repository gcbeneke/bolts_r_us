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
movepos = refpos1
movement = [0, 0, 0, 0, 0, 0]
## Ophalen van knoppenstatus
def state_callback(msg):
 	global status
	status = msg.data
	#print status

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
	beweeg = 2
	bJointtemp = [i * beweeg for i in jRad]
	bjointtemp1 = [w / 5 for w in bJointtemp]
	bJoint = [z + v for z, v in zip(bjointtemp1,bJoint1)]
	return bJoint

def calculateToRefpos1(currentPos, x):
	offsetJ = [i - j for i, j in zip(refpos1,currentPos)]
	    #jRad = offsetJ /afstandtotj
	bMovement = [w / 5 for w in offsetJ]
	bMovement = [w * x for w in bMovement]
	updatedCurrentPos = [z + v for z, v in zip(bMovement,currentPos)]
	return updatedCurrentPos

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

def movestap(x):
    global movement
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
    else:
        start = False
        stop = False
    try:
        if start == True:
            print temp
            for x in range(5):
                print x
                rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
                if status == 1:
            		joint_states = rospy.wait_for_message("joint_states", JointState)
            		joints_pos = joint_states.position
            		movepos = joints_pos
            		print movepos
            		x = temp + 1
            		movement = calculateToRefpos1(movepos, x)
            		movepos = movement
            		#print movement
            		g.trajectory.points = [
            	   	    	JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
            	    	   	JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0))]

            	    	client.send_goal(g)
                    	client.wait_for_result()
                elif status == 2:
                    temp = x
                    break
                if x == 5:
                    ready = True
                elif x < 5:
                    ready = False
        return ready
            				#gevraagde positie:
    except KeyboardInterrupt:
		client.cancel_goal()
		raise
    except:
    	raise

def main():
    global client
    try:
        x = 0
        counter = 0
        rospy.init_node("test_move", anonymous=True, disable_signals=True)
    	rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
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
            klaar = movestap(x)
            if klaar == True:
                break
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
