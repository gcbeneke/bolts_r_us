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

## Alle belangrijke jointstates
movement = [0, 0, 0, 0, 0, 0]
refPos = [-0.05583, 1.22699, -0.18286,0.78646, -1.20635, -0.52067] # positie 1 (0 punt)
refPos2 = [0.04141, 1.37890, -0.50648, 0.93691,-1.13694,-0.70177] # positie 2
boltPos = [0.52298, 0.82716, 0.16881, 0.02369, 0.52621, -0.42037]
safeBoltPos = [0.52299, 0.63573, 0.15993, 0.01783, 0.72653, -0.41322]

## Declareren globale variabelen
# afstand tussen pos 1 en pos 2
afstandtotj = 6.45
status = 0
movepos = refPos
statusRobot = 0

## Ophalen van knoppenstatus
def state_callback(msg):
 	global status
	status = msg.data

## Ophalen van gatpositie
def hole_position_callback(data):
 	global holePos
	holePos = data.data

## Ophalen van robotstatus
def robot_state_callback(data):
    global new_robot_status
    global statusRobot
    new_robot_status = data.data
    statusRobot = new_robot_status

## methode voor het berekenen voor de verschil tussen gewenst en huidige joint positie
## Geeft als return het verschil
def calculateOffSet(currentPos, wantedPos):
    offsetJ = [i - j for i, j in zip(wantedPos,currentPos)]
    return offsetJ

## Berekenen van de nieuwe positie
## Returned de nieuwe positie
def calculateToPosition(currentPos, wantedPos):
	offsetJ = [i - j for i, j in zip(wantedPos,currentPos)]
	updatedCurrentPos = [z + v for z, v in zip(offsetJ,currentPos)]
	return updatedCurrentPos

## Berekent de gatpositie
## De robot en camera moeten gekalibreerd zijn voordat deze functie uitgevoerd kan worden
def calculateHolePosition(currentPos):
    global holePos
    rospy.subscriber("bru_vis_calibratedPos", Int8, hole_position_callback)

    ## Berekent de benodige bewegingen
    movePerCm = calculateMoment()

    ## Berekent de gewenste joint beweging
    wantedPos = calculateWantedPos(currentPos, holePos, movePerCm)
    return wantedPos

## Berekent de joint bewegingen per cm
## returned de joint bewegingen per cm
def calculateMoment():
    offsetJ = [i - j for i, j in zip(refpos2,refpos1)]
    jRad = [x / afstandtotj for x in offsetJ]
    return jRad

## Berekent de joint bewegingen met het aantal meegegeven cm
## Returned de joint bewegigen met het aantal meegegeven cm
def calculateWantedPos(currentPos, holePos, movePerCm):
    wantedMovement = [i * holePos for i in movePerCm]
    wantedPos = [z + v for z, v in zip(wantedMovement, currentPos)]
    return wantedPos

client = None

def moveToWarehouse():
    ## Declareren globale variabelen
    global statusRobot
    global movepos
    global joints_pos
    global status

    ## Declareren lokale variabelen
    i = 0

    ## Initialisatie robot
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES

    ## Status Ophalen
    ## 1 = Start, 2 = Stop
    rospy.Subscriber("bru_ctrl_state", Int8, state_callback)

    try:
        ## Controleren status
        if status == 1:
            ## Huidige joint positie opvragen
            joint_states = rospy.wait_for_message("joint_states", JointState)
            joints_pos = joint_states.position
            movepos = joints_pos

            ## Gevraagde beweging uitrekenen
            movement = calculateToPosition(movepos, boltPos)
            movepos = movement

            ## Bewegen naar gevraagde positie
            g.trajectory.points = [
                    JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
                    JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0))]

            client.send_goal(g)
            client.wait_for_result()

        ## Huidige joint positie opvragen
        joint_states = rospy.wait_for_message("joint_states", JointState)
        joints_pos = joint_states.position

        ## Uitrekenen verschil in gewenste en oude joints
        offset = calculateOffSet(joints_pos, movepos)

        ## Controleren op de correctheid van de Joints
        for x in offset:
            if x < 0.001 and x > -0.001:
                i = i + 1
            if i > 5:
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
    ## Declareren globale variabelen
    global statusRobot
    global movepos
    global joints_pos
    global status

    ## Declareren lokale variabelen
    i = 0

    ## Initialisatie robot
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES

    ## Status Ophalen
    ## 1 = Start, 2 = Stop
    rospy.Subscriber("bru_ctrl_state", Int8, state_callback)

    try:
        ## Controleren status
        if status == 1:
            ## Huidige joint positie opvragen
            joint_states = rospy.wait_for_message("joint_states", JointState)
            joints_pos = joint_states.position
            movepos = joints_pos

            ## Gevraagde beweging uitrekenen
            movement = calculateToPosition(movepos, safeBoltPos)
            movepos = movement

            ## Bewegen naar gevraagde positie
            g.trajectory.points = [
                    JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
                    JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0))]

            client.send_goal(g)
            client.wait_for_result()

        ## Huidige joint positie opvragen
        joint_states = rospy.wait_for_message("joint_states", JointState)
        joints_pos = joint_states.position

        ## Uitrekenen verschil in gewenste en oude joints
        offset = calculateOffSet(joints_pos, movepos)

        ## Controleren op de correctheid van de Joints
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
    ## Declareren globale variabelen
    global statusRobot
    global movepos
    global joints_pos
    global status

    ## Declareren lokale variabelen
    i = 0

    ## Initialisatie robot
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES

    ## Status Ophalen
    ## 1 = Start, 2 = Stop
    rospy.Subscriber("bru_ctrl_state", Int8, state_callback)

    try:
        ## Controleren status
        if status == 1:
            ## Huidige joint positie opvragen
            joint_states = rospy.wait_for_message("joint_states", JointState)
            joints_pos = joint_states.position
            movepos = joints_pos

            ## Gevraagde beweging uitrekenen
            movement = calculateToPosition(movepos, refPos)
            movepos = movement

            ## Bewegen naar gevraagde positie
            g.trajectory.points = [
                    JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
                    JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0))]

            client.send_goal(g)
            client.wait_for_result()

        ## Huidige joint positie opvragen
        joint_states = rospy.wait_for_message("joint_states", JointState)
        joints_pos = joint_states.position

        ## Uitrekenen verschil in gewenste en oude joints
        offset = calculateOffSet(joints_pos, movepos)

        ## Controleren op de correctheid van de Joints
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
        rospy.init_node("moveRobot", anonymous=True, disable_signals=True)
    	rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
        rospy.Subscriber("bru_irb_new_robotState", Int8, robot_state_callback)
        pub = rospy.Publisher('bru_irb_robotState', Int8, queue_size=10)
        rate = rospy.Rate(10)

        client = actionlib.SimpleActionClient('joint_trajectory_action', FollowJointTrajectoryAction)
        client.wait_for_server()

        ## User interface
        ## 1. Start
        ## 2. Stop
        ## 3. Calibrate
        print ""
        print "Connected to ABB IRB120"
        print ""
        print "Choose what to do:"
        print "- Press the calibratebutton to calibrate"
        print "- Press the startbutton to start"
        print "- Press the stopbutton to quit the program"

        parameters = rospy.get_param(None)

        ## Programma dat wordt uitgevoerd
        while not rospy.is_shutdown():
            pub.publish(statusRobot)
            rate.sleep()
            if statusRobot == 2:
                moveToWarehouse()
            elif statusRobot == 4 or statusRobot == 1:
                moveAboveBolt()
            elif statusRobot == 5:
                moveBoltToHole()

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
