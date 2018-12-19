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

JOINT_NAMES = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
avg_value = [0, 0, 0, 0, 0, 0]
current_value = [0,0,0,0,0,0]
statusRobot = 6
new_robot_status = 0

firstPos  = [-0.90279, 1.00068, 0.37982, -0.90743, -1.47271, 0.05792]
secondPos = [-0.83944, 1.03169, 0.29536, -0.84939, -1.42815, 0.09053]
thirdPos = [-0.78646, 0.94316, 0.55527, -0.78557, -1.53922, -0.04047]
fourthPos = [-0.77261, 1.01772, 0.52081, -0.76527, -1.58833, -0.01226]

pos02 = [-0.86438, 0.97722, 0.44759, -0.86636, -1.49561, 0.01943]
pos24 = [-0.82681, 0.95869, 0.50449, -0.82708, -1.51736, -0.01251]
pos46 = [-0.78623,0.94235, 0.55824, -0.78587, -1.54050, -0.04180]
pos68 = [-0.73675, 0.92700, 0.61260, -0.73576, -1.56705, -0.07064]
pos810 = [-0.68294, 0.91418, 0.66279, -0.68224, -1.59497, -0.09548]

forwardPos02 = [-0.80140, 1.00637, 0.36427, -0.80848, -1.45168, 0.05239]
forwardPos24 = [-0.76444, 0.98774, 0.41694, -0.76897, -1.47092, 0.02327]
forwardPos46 = [-0.72033, 0.96876, 0.47324, -0.72281, -1.49401, -0.00695]
forwardPos68 = [-0.67407, 0.95323, 0.52210, -0.67506, -1.51618, -0.03232]
forwardPos810 = [-0.62585, 0.93971,0.56725, -0.62603, -1.53895, -0.05449]

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

## methode voor het berekenen voor de verschil tussen gewenst en huidige joint positie
## Geeft als return het verschil
def calcpos02(cm):
    global firstPos
    global pos02
    offsetJ = [i - j for i, j in zip(pos02,firstPos)]
    step = [i / 3.3 for i in offsetJ]
    newPos = [0,0,0,0,0,0]
    stepSet = [j * cm for j in step]
    newPos = [k + l for k, l in zip(stepSet, firstPos)]
    return newPos

def calcForward(cm, pos):
    if cm <= 2:
        offsetJ = [i - j for i, j in zip(forwardPos02,pos02)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, pos)]
        return newPos
    elif cm <= 4 and cm > 2:
        offsetJ = [i - j for i, j in zip(forwardPos24,pos24)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, pos)]
        return newPos
    elif cm <= 6 and cm > 4:
        offsetJ = [i - j for i, j in zip(forwardPos46,pos46)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, pos)]
        return newPos
    elif cm <= 8 and cm > 6:
        offsetJ = [i - j for i, j in zip(forwardPos68,pos68)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, pos)]
        return newPos
    elif cm <= 10 and cm > 8:
        offsetJ = [i - j for i, j in zip(forwardPos810,pos810)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, pos)]
        return newPos

def calcpos24(cm):
    global pos02
    global pos24
    offsetJ = [i - j for i, j in zip(pos24,pos02)]
    step = [i / 2 for i in offsetJ]
    newPos = [0,0,0,0,0,0]
    cm = cm - 2
    stepSet = [j * cm for j in step]
    newPos = [k + l for k, l in zip(stepSet, pos02)]
    return newPos

def calcpos46(cm):
    global pos46
    global pos24
    offsetJ = [i - j for i, j in zip(pos46,pos24)]
    step = [i / 2 for i in offsetJ]
    newPos = [0,0,0,0,0,0]
    cm = cm - 4
    stepSet = [j * cm for j in step]
    newPos = [k + l for k, l in zip(stepSet, pos24)]
    return newPos

def calcpos68(cm):
    global pos46
    global pos68
    offsetJ = [i - j for i, j in zip(pos68,pos46)]
    step = [i / 2 for i in offsetJ]
    newPos = [0,0,0,0,0,0]
    cm = cm - 6
    stepSet = [j * cm for j in step]
    newPos = [k + l for k, l in zip(stepSet, pos46)]
    return newPos

def calcpos810(cm):
    global pos810
    global pos68
    offsetJ = [i - j for i, j in zip(pos810,pos68)]
    step = [i / 2 for i in offsetJ]
    newPos = [0,0,0,0,0,0]
    cm = cm - 8
    stepSet = [j * cm for j in step]
    newPos = [k + l for k, l in zip(stepSet, pos68)]
    return newPos

def calculateForwardStep(pos):
    global firstPos
    global secondPos
    offsetJ = [i - j for i, j in zip(secondPos, firstPos)]
    step = [i / 3.1 for i in offsetJ]
    newPos = [0,0,0,0,0,0]
    stepSet = [j * 3.1 for j in step]
    newPos = [k + l for k, l in zip(stepSet, pos)]
    return newPos

## Beweegt de robot naar de meegegeven joint positie
def moveRobot():
    global firstPos
    global statusRobot
    cm = 4.1
    try:
        joint_states = rospy.wait_for_message("joint_states", JointState)
        joints_pos = joint_states.position
        g = FollowJointTrajectoryGoal()
        g.trajectory = JointTrajectory()
        g.trajectory.joint_names = JOINT_NAMES
        cm = cm - 2.05
        if cm <= 2:
            pos = calcpos02(cm)
        elif cm <= 4 and cm > 2:
            pos = calcpos24(cm)
        elif cm <= 6 and cm > 4:
            pos = calcpos46(cm)
        elif cm <= 8 and cm > 6:
            pos = calcpos68(cm)
        elif cm <= 10 and cm > 8:
            pos = calcpos810(cm)
        newerPos = calcForward(cm, pos)
            ## Bewegen naar gevraagde positie
        g.trajectory.points = [
                JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
                JointTrajectoryPoint(positions=firstPos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(2.0)),
                JointTrajectoryPoint(positions=pos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(4.0)),
                JointTrajectoryPoint(positions=newerPos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(6.0))]

        client.send_goal(g)
        client.wait_for_result()
        statusRobot = 11
    except KeyboardInterrupt:
        client.cancel_goal()
        raise
    except:
        raise

def main():
    global client
    global statusRobot
    try:
        ## Initieren van de node
        rospy.init_node("optoForceRobot", anonymous=True, disable_signals=True)
        ## Publisher aanmaken
        client = actionlib.SimpleActionClient('joint_trajectory_action', FollowJointTrajectoryAction)
        client.wait_for_server()
        parameters = rospy.get_param(None)
        ## Programma dat wordt uitgevoerd
        while not rospy.is_shutdown():
            if statusRobot == 6 and statusRobot != 11:
                moveRobot()
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
