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
from vision.msg import *

JOINT_NAMES = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
avg_value = [0, 0, 0, 0, 0, 0]
current_value = [0,0,0,0,0,0]
statusRobot = 0
new_robot_status = 0

x = 0
y = 0
xcm = 0
ycm = 0

firstPos  = [-0.90280, 1.03482, 0.36274, -0.90629, -1.48322, 0.04448]
secondPos = [-0.83944, 1.03169, 0.29536, -0.84939, -1.42815, 0.09053]
thirdPos = [-0.78646, 0.94316, 0.55527, -0.78557, -1.53922, -0.04047]
fourthPos = [-0.77261, 1.01772, 0.52081, -0.76527, -1.58833, -0.01226]
betweenPos = [-0.35746, -0.06283, 1.02381, -0.42115, -1.02429, 0.14476]
betweenBetweenPos = [-1.17539, 0.95437, 0.64187, -1.17471, -1.60005, -0.11492]

pos02 = [-0.86822, 1.01444, 0.42402, -0.86938, -1.50492, 0.00930]
pos24 = [-0.83040, 0.99639, 0.48190, -0.83018, -1.52802, -0.02344]
pos46 = [-0.78310,0.97867, 0.54351, -0.78217, -1.55594, -0.05735]
pos68 = [-0.73601, 0.96520, 0.59522, -0.73580, -1.58262, -0.08453]
pos810 = [-0.68453, 0.95403, 0.64295, -0.68507, -1.61059, -0.10802]

forwardPos02 = [-0.83683, 1.02740, 0.38491, -0.83954, -1.48422, 0.02625]
forwardPos24 = [-0.79625, 1.00760, 0.44589, -0.79693, -1.50822, 0.00764]
forwardPos46 = [-0.75039, 0.98985, 0.50445, -0.74972, -1.53425, -0.03932]
forwardPos68 = [-0.70333, 0.97556, 0.55551, -0.70231, -1.55989, -0.06576]
forwardPos810 = [-0.65323, 0.96376, 0.60159, -0.65244, -1.58585, -0.08806]

forwardForwardPos00 = [-0.84270, 1.06293, 0.28343, -0.85089, 1.44176, 0.07650]
forwardForwardPos02 = [-0.80490, 1.04240, 0.34123, -0.80985, -1.46059, 0.04371]
forwardForwardPos24 = [-0.76326, 1.02273, 0.39922, -0.76581, -1.48257, 0.02679]
forwardForwardPos46 = [-0.72321, 1.00148, 0.46570, -0.72359, -1.51244, 0.02288]
forwardForwardPos68 = [-0.66589, 0.99137, 0.49940, -0.66569, -1.52712, -0.04198]
forwardForwardPos810 = [-0.61780, 0.97806, 0.54641, -0.61716, -1.55230, -0.06455]

verh2cm = 1.385
verh4cm = 1.227
verh6cm = 0.98
verh8cm = 0.96
verh10cm = 1.0425




def verhoudingPixelWaarde(xcm):
    cm = xcm
    if cm >= 0 and cm < 2:
        print " hallo"
    elif cm >= 2 and cm < 4:
        diff = cm - 2.77
        diff = diff / 2
        verhouding = diff * (verh2cm-verh4cm)
        verhouding =  verh2cm - verhouding
        cm = xcm / verhouding
        cm = cm - (diff*0.5)
        return cm
    elif cm >= 4 and cm < 6:
        diff = cm - 4.93
        diff = diff / 2
        verhouding = diff * 0.8
        verhouding = verh4cm - verhouding
        cm = verhouding * xcm
        print verhouding
        print cm
        cm = cm - 2.0
        return cm
    elif cm >= 6 and cm < 8:
        0.4
    elif cm >= 8 and cm < 10:
        0.2


## roteren van de bout voor 2cm (1ste keer)
rotatebol02 = [-0.69212, 1.08465, 0.16088, -0.71441, -1.34153, 0.11911]
## KOMT NOG EEN POSITIE VOOR BOUT INDRAAIEN 2CM (2DE KEER)( VERDER ERINDRAAIEN)

def verhouding():
    x1 = 125.05
    x2 = 416.82
    y1 = 206.54
    y2 = 60.59

    xVerschil = x2 - x1
    yVerschil = y1 - y2

    horizontalDistance = 17.1
    verticalDistance = 7.4

    xVerhouding = horizontalDistance/xVerschil
    yVerhouding = verticalDistance/yVerschil
    ##print xVerhouding
    return xVerhouding

## Ophalen van knoppenstatus
def state_callback(msg):
 	global status
	status = msg.data

## controleren of de robot bij de gevraagde positie is
def calculateOffSet(currentPos, wantedPos):
    offsetJ = [i - j for i, j in zip(wantedPos,currentPos)]
    return offsetJ

## Ophalen van robotstatus
def robot_state_callback(data):
    global new_robot_status
    global statusRobot
    new_robot_status = data.data
    statusRobot = new_robot_status
    #print "Robotstatus: ", statusRobot

def moveUntilForce():
        offsetJ = [i - j for i, j in zip(forwardPos24,pos24)]
        step = [i / 1.5 for i in offsetJ]
        newPos = [0,0,0,0,0,0]
        stepSet = [j * 4 for j in step]
        newPos = [k + l for k, l in zip(stepSet, pos24)]
        return newPos

def rotatebolt():
        offsetJ = [i - j for i, j in zip(rotatebol02,forwardPos02)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, forwardPos02)]
        return newPos

def calcForwardForward(cm, pos):
    if cm <= 2:
        offsetJ = [i - j for i, j in zip(forwardForwardPos02,forwardPos02)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, pos)]
        return newPos
    elif cm <= 4 and cm > 2:
        offsetJ = [i - j for i, j in zip(forwardForwardPos24,forwardPos24)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, pos)]
        return newPos
    elif cm <= 6 and cm > 4:
        offsetJ = [i - j for i, j in zip(forwardForwardPos46,forwardPos46)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, pos)]
        return newPos
    elif cm <= 8 and cm > 6:
        offsetJ = [i - j for i, j in zip(forwardForwardPos68,forwardPos68)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, pos)]
        return newPos
    elif cm <= 10 and cm > 8:
        offsetJ = [i - j for i, j in zip(forwardForwardPos810,forwardPos810)]
        newPos = [0,0,0,0,0,0]
        newPos = [k + l for k, l in zip(offsetJ, pos)]
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

## methode voor het berekenen voor de verschil tussen gewenst en huidige joint positie
## Geeft als return het verschil
def calcpos02(cm):
    global firstPos
    global pos02
    offsetJ = [i - j for i, j in zip(pos02,firstPos)]
    step = [i / 2 for i in offsetJ]
    newPos = [0,0,0,0,0,0]
    #cm = cm - 2
    stepSet = [j * cm for j in step]
    newPos = [k + l for k, l in zip(stepSet, firstPos)]
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

def robot_currentValues_callback(msg):
    global current_value
    global statusRobot
    current_value[0] = msg.fx
    current_value[1] = msg.fy
    current_value[2] = msg.fz
    current_value[3] = msg.tx
    current_value[4] = msg.ty
    current_value[5] = msg.tz
    if current_value[2] < -5000:
        statusRobot = 7

def callback_xy_values(msg):
    global x
    global y
    global xcm
    global ycm

    x1 = 125.05
    y1 = 189.98

    x = msg.allHolesDataVec[0].x
    y = msg.allHolesDataVec[0].y

    #print "Waarde voor x: ", x
    #print "Waarde voor y: ", y

    xVer = x - x1
    yVer = y1 - y
    xVerhouding = verhouding()
    xcm = xVer * xVerhouding
    #ycm = yVer * yVerhouding
    print "gemeten cm: ", xcm
    xcm = verhoudingPixelWaarde(xcm)
    print "berekende cm: ", xcm

## Beweegt de robot naar de meegegeven joint positie
def moveRobot():
    global firstPos
    global statusRobot
    global xcm
    xcm = 4.05
    i = 0
    try:
        if xcm != 0:
            cm = xcm
            joint_states = rospy.wait_for_message("joint_states", JointState)
            joints_pos = joint_states.position
            g = FollowJointTrajectoryGoal()
            g.trajectory = JointTrajectory()
            g.trajectory.joint_names = JOINT_NAMES
            #cm = xcm - 2.05
            ##print xcm
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
            newerNewerPos = calcForwardForward(cm, newerPos)
            ##print "Positie:", pos
            ##print "Positie voor:", newerPos
                ## Bewegen naar gevraagde positie
            g.trajectory.points = [
                    JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
                    JointTrajectoryPoint(positions=betweenPos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(1.0)),
                    JointTrajectoryPoint(positions=betweenBetweenPos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(2.0)),
                    JointTrajectoryPoint(positions=firstPos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(3.0)),
                    ## pos
                    ## newerPos
                    JointTrajectoryPoint(positions=pos46, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(5.0)),
                    JointTrajectoryPoint(positions=forwardPos46, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(7.0))]
                    #JointTrajectoryPoint(positions=newerNewerPos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(9.0))]
                    ##JointTrajectoryPoint(positions=rotatePos, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(8.0))]
            client.send_goal(g)
            client.wait_for_result()
            ##offset = calculateOffSet(joints_pos, newerPos)
            ##for x in offset:
                ##if x < 0.001 and x > -0.001:
                ##    i = i + 1
                ##if i > 5:
            print " ik ga naar voren voor de correctie!"
            statusRobot = 235
    except KeyboardInterrupt:
        client.cancel_goal()
        raise
    except:
        raise

def rotatebolt():
    global statusRobot
    holeposition = moveUntilForce()
    joint_states = rospy.wait_for_message("joint_states", JointState)
    joints_pos = joint_states.position
    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = JOINT_NAMES
    g.trajectory.points = [
            JointTrajectoryPoint(positions=joints_pos, velocities=[1]*6, accelerations=[1], effort = [0],  time_from_start=rospy.Duration(0.0)),
            JointTrajectoryPoint(positions=holeposition, velocities=[1]*6, accelerations=[1], effort = [0], time_from_start=rospy.Duration(2.0))]
    client.send_goal(g)
    client.wait_for_result()

def main():
    global client
    global statusRobot
    try:
        ## Initieren van de node
        rospy.init_node("optoForceRobot", anonymous=True, disable_signals=True)
        rospy.Subscriber("bru_irb_robotState", Int8, robot_state_callback)
        rospy.Subscriber("bru_vis_holeData", imageCircleData, callback_xy_values)
        ## Publisher aanmaken
        client = actionlib.SimpleActionClient('joint_trajectory_action', FollowJointTrajectoryAction)
        ##client.wait_for_server()
        parameters = rospy.get_param(None)
        ## Programma dat wordt uitgevoerd
        while not rospy.is_shutdown():
            rospy.Subscriber("bru_irb_new_robotState", Int8, robot_state_callback)
            rospy.Subscriber("bru_opt_workData", OptoForceData, robot_currentValues_callback)
            if statusRobot == 5:
                moveRobot()
            elif statusRobot == 6:
                rotatebolt()
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
