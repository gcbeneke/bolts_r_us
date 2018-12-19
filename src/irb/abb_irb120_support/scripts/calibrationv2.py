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
params.minThreshold = 140;
params.maxThreshold = 255;

# Filter by Area.
params.filterByArea = True
params.minArea = 20

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.85

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

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

JOINT_NAMES = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']
pi = 3.14
homePosition = [0,0,0,0,0,0]
calibrationToCamera = False
## Alle jointsstates voor de eerste positie
status = 0
movement = [0, 0, 0, 0, 0, 0]
statusRobot = 0
alwaysTrue = True
posBottomLeft = [0.11984, 1.14822, 0.49917,0.90106, -1.65097, -0.08359]
posTopLeft = [0.11984, 0.76255, 0.68557, 0.89825, -1.52681, -0.23960]
posBottomRight = [0.32488, 1.36717, -0.29109, 1.18545,-1.31537,-0.62547]
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
    global cv2_img
    print ("Druk op y om naar het 1ste punt te kalibreren")
    inp = raw_input("")[0]
    if inp == 'y':
        position(posBottomLeft)
        time.sleep(2)
        getKeypoint(cv2_img)
        bottomright()

def bottomright():
    global posBottomRight
    global cv2_img
    print ("Druk op y om naar het 2de punt te kalibreren")
    inp = raw_input("")[0]
    if inp == 'y':
        position(posBottomRight)
        time.sleep(2)
        getKeypoint(cv2_img)
        topLeft()

def topLeft():
    global posTopLeft
    global cv2_img
    print ("Druk op y om naar het 3de punt te kalibreren")
    inp = raw_input("")[0]
    if inp == 'y':
        position(posTopLeft)
        time.sleep(2)
        getKeypoint(cv2_img)
        print(keypointsGlobal[0].pt[0])
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

# Function to retrieve one keypoint on every ABB calibration position
def getKeypoint(cv2_img):
    global keypointsGlobal
    # Convert the image to a grayscale image
    gray_image = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)

    # Detect blobs in the grayscale image
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
        cv2.imshow("Videostream", im_with_keypoints)
        cv2.waitKey(30)


def main():
    global client
    global statusRobot
    global calibrationToCamera

    try:
        x = 0
        counter = 0
        rospy.init_node("calibrateRobot", anonymous=True, disable_signals=True)
    	rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
        rospy.Subscriber("bru_irb_new_robotState", Int8, robot_state_callback)
        rospy.Subscriber("/camera/color/image_raw", Image, image_callback)
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
