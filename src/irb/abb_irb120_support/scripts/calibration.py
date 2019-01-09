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
import numpy as np
import cv2
import sys

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 55;
params.maxThreshold = 255;

# Filter by Area.
params.filterByArea = True
params.minArea = 30

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.85

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

JOINT_NAMES = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
pi = 3.14
homePosition = [0,0,0,0,0,0]
calibrationToCamera = False
## Alle jointsstates voor de eerste positie
calibrationstate = 0
status = 0
movement = [0, 0, 0, 0, 0, 0]
statusRobot = 0
alwaysTrue = True
posBottomLeft = [-0.90280, 1.03482, 0.36274, -0.90629, -1.48322, 0.04448]
posTopLeft = [-0.90121, 0.75491, 0.46869, -0.92426, -1.37668, 0.18342]
posBottomRight = [-0.45062, 0.93036, 0.78268, -0.45461, -1.71852, -0.15392]
boltPos = [1.10464, 0.49386, 0.81989, -0.00839, 0.23239, -0.51316]
safeBoltPos = [1.10464, -0.00791, 0.71832, -0.00259, 0.83561, -0.51956]
betweensafepos = [1.10465, 0.18023, 0.81070, -0.00360, 0.55544, -0.51815]
betweenPos = [-0.35746, -0.06283, 1.02381, -0.42115, -1.02429, 0.14476]

def callback_calibration_status(msg):
    global calibrationstate
    calibrationstate = msg.data

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

def moveAboveBolt():
    if status == 3:
        position(safeBoltPos)

def betweenCalibration():
    if status == 3:
        position(betweenPos)

def moveBetweensafe():
    global calibrationstate
    if status == 3:
        position(betweensafepos)

def moveToWarehouse():
    global calibrationstate
    if status == 3:
        position(boltPos)

def bottomLeft():
    global posBottomLeft
    global status
    print ("Druk op y om naar het 1ste punt te kalibreren")
    inp = raw_input("")[0]
    if inp == 'y':
        if status == 3:
            position(posBottomLeft)
            time.sleep(3)
            getKeypoint(cv2_img)
            print "x is :", keypointsGlobal[0].pt[0], " y is : ", keypointsGlobal[0].pt[1]

def bottomRight():
    global posBottomRight
    global status
    print ("Druk op y om naar het 2de punt te kalibreren")
    inp = raw_input("")[0]
    if inp == 'y':
        if status == 3:
            position(posBottomRight)
            time.sleep(3)
            getKeypoint(cv2_img)
            print "x is :", keypointsGlobal[1].pt[0], " y is : ", keypointsGlobal[1].pt[1]

def topLeft():
    global posTopLeft
    global calibrationstate
    print ("Druk op y om naar het 3de punt te kalibreren")
    inp = raw_input("")[0]
    if inp == 'y':
        if status == 3:
            position(posTopLeft)
            time.sleep(3)
            getKeypoint(cv2_img)
            print "x is :", keypointsGlobal[2].pt[0], " y is : ", keypointsGlobal[2].pt[1]

def homeposition():
    global homePosition
    global calibrationToCamera
    print ("Druk op y om naar het homepunt te gaan")
    inp = raw_input("")[0]
    if inp == 'y':
        if status == 3:
            position(homePosition)
            calibrationToCamera = True
            pub = rospy.Publisher("bru_irb_new_robotState", Int8, queue_size=1)
            robotstate = 1
            pub.publish(robotstate)

def position(wantedPos):
    global calibrationstate
    joint_states = rospy.wait_for_message("joint_states", JointState)
    joints_pos = joint_states.position
    movepos = joints_pos
    i = 0
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
    offset = calculateOffSet(joints_pos, wantedPos)
    for x in offset:
        if x < 0.001 and x > -0.001:
            i = i + 1
        if i > 5:
            calibrationstate = calibrationstate + 1

def calibration(wantedPos):
    global joints_pos
    global status
    global statusRobot
    global alwaysTrue
    global calibrationToCamera
    global calibrationstate
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
                            if i > 5:
                                 calibrationstate = 1
    except KeyboardInterrupt:
            client.cancel_goal()
            raise
    except:
        	raise

    # Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else :
    detector = cv2.SimpleBlobDetector_create(params)

# Create global bridge variable to convert ROS and OpenCV images
bridge = CvBridge()
keypointsGlobal = []

global cv2_img

# Function to retrieve one keypoint on every ABB calibration position
def getKeypoint(cv2_img):
    global keypointsGlobal
    # Convert the image to a grayscale image
    gray_image = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)

    # Detect blobs in the grayscale image
    keypoints = detector.detect(gray_image)

    while not keypoints:
        keypoints = detector.detect(gray_image)

    # Add the keypoint to a vector with 3 keypoints
    keypointsGlobal.append(keypoints[0])


def image_callback(image):
    try:
        global cv2_img
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(image, "bgr8")

    except CvBridgeError, e:
        print(e)

    else:
        # Convert the image to a grayscale image
        gray_image = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)

        # Detect blobs in the grayscale image
        keypoints = detector.detect(gray_image)

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        im_with_keypoints = cv2.drawKeypoints(cv2_img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Show the image with a circle drawn over the bolt
        #cv2.imshow("Videostream", im_with_keypoints)
        #cv2.waitKey(30)


def main():
    global client
    global statusRobot
    global calibrationToCamera
    global status

    try:
        x = 0
        counter = 0
        rospy.init_node("calibrateRobot", anonymous=True, disable_signals=True)
    	rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
        rospy.Subscriber("bru_irb_new_robotState", Int8, robot_state_callback)
        rospy.Subscriber("bru_irb_calibrationState", Int8, callback_calibration_status)
        rospy.Subscriber("/camera/color/image_raw", Image, image_callback)
        pub = rospy.Publisher('bru_irb_robotState', Int8, queue_size=10)
        pubcali = rospy.Publisher("bru_irb_calibrationState", Int8, queue_size=10)
        rate = rospy.Rate(10)

        client = actionlib.SimpleActionClient('joint_trajectory_action', FollowJointTrajectoryAction)
        client.wait_for_server()
        print ""
        parameters = rospy.get_param(None)
        while not rospy.is_shutdown():
            #pub.publish(statusRobot)

            rate.sleep()
            if calibrationToCamera == False and calibrationstate == 0:
                calibrationhome()
            elif calibrationstate == 1:
                moveAboveBolt()
            elif calibrationstate == 2 or calibrationstate == 5:
                moveBetweensafe()
            elif calibrationstate == 3:
                moveToWarehouse()
                pubcali.publish(calibrationstate)
            elif calibrationstate == 6:
                moveAboveBolt()
            elif calibrationstate == 7:
                betweenCalibration()
            elif calibrationstate == 8:
                bottomLeft()
            elif calibrationstate == 9:
                bottomRight()
            elif calibrationstate == 10:
                topLeft()
            elif calibrationstate == 11:
                homeposition()
            elif calibrationstate == 12:
                break

            index = str(parameters).find('prefix')
            if (index > 0):
                prefix = str(parameters)[index+len("prefix': '"):(index+len("prefix': '")+str(parameters)[index+len("prefix': '"):-1].find("'"))]
                for i, name in enumerate(JOINT_NAMES):
                    JOINT_NAMES[i] = prefix + name

    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise


if __name__ == '__main__': main()
