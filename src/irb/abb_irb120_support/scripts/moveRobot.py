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
boltPos = [1.10464, 0.48894, 0.82054, -0.00813, 0.23652, -0.51340]
safeBoltPos = [1.10464, -0.00791, 0.71832, -0.00259, 0.83561, -0.51956]
betweenPos = [-0.35746, -0.06283, 1.02381, -0.42115, -1.02429, 0.14476]
betweensafepos = [1.10465, 0.18023, 0.81070, -0.00360, 0.55544, -0.51815]


x_pos1 = [0.11902, 1.22865, -0.15359, 0.14567, -0.95006, -0.14157]
x_pos2 = [0.10470, 1.44064, -0.60579, 0.15998, -0.71131, -0.17982]
afstandPos1totPos2 = 6.4
## Declareren globale variabelen
# afstand tussen pos 1 en pos 2
afstandtotj = 6.45
status = 0
movepos = refPos
statusRobot = 0
new_robot_status = 0

## Ophalen van knoppenstatus
def state_callback(msg):
 	global status
	status = msg.data

## Ophalen van gatpositie
def hole_position_callback(data):
 	global holePos
	holePos = data.data

## Ophalen van robotstatus
def robot_state_callback(msg):
    global statusRobot
    statusRobot = msg.data

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
                    JointTrajectoryPoint(positions=betweensafepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0)),
                    JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(2.0))]

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
            if statusRobot == 1:
                g.trajectory.points = [
                        JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
                        JointTrajectoryPoint(positions=betweenPos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(2.0)),
                        JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(4.0))]

                client.send_goal(g)
                client.wait_for_result()
            if statusRobot == 4:
                g.trajectory.points = [
                        JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
                        JointTrajectoryPoint(positions=betweensafepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(2.0)),
                        JointTrajectoryPoint(positions=movepos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(4.0))]

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

def main():
    global client
    global statusRobot
    statusRobot = 1
    try:
        rospy.init_node("moveRobot", anonymous=True, disable_signals=True)
    	rospy.Subscriber("/bru_ctrl_state", Int8, state_callback)
        #rospy.Subscriber("bru_irb_robotState", Int8, robot_state_callback)
        pub = rospy.Publisher('bru_irb_robotState', Int8, queue_size=2)
        rospy.Subscriber("/bru_irb_robotState", Int8, robot_state_callback)

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
            rospy.Subscriber("bru_irb_robotState", Int8, robot_state_callback)
            if statusRobot == 2:
                moveToWarehouse()
                #print statusRobot
                pub.publish(statusRobot)
            elif statusRobot == 4 or statusRobot == 1:

                moveAboveBolt()
                #print statusRobot
                #pub.publish(statusRobot)
            elif statusRobot == 5:
                #print statusRobot
                pub.publish(statusRobot)
                statusRobot = 200
                break

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
