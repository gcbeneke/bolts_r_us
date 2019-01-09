#!/usr/bin/env python
import roslib;
import sys
import rospy
import math
from std_srvs.srv import Trigger
from weiss_gripper_ieg76.srv import *
from std_msgs.msg import Int8


calibrationstate = 0
new_robot_status = 0
opened = False

def callback_calibration_status(msg):
	global calibrationstate
	pub = rospy.Publisher("bru_irb_calibrationState", Int8, queue_size=1)
	calibrationstate = msg.data
	try:
		if calibrationstate == 4:
			send_grasp_object_request(0)
			calibrationstate = 5
			pub.publish(calibrationstate)
	except rospy.ServiceException, e:
			print "Service call failed: %s"%e

def state_callback(msg):
	global opened
	status = msg.data
	try:
			if status == 3:
				send_reference_request()
				send_open_request(16)
			if status == 1 and opened == False:
				send_reference_request()
				send_open_request(16)
				opened = True

	except rospy.ServiceException, e:
			print "Service call failed: %s"%e

def callback_robot_status(data):
	global new_robot_status
	pub = rospy.Publisher("bru_irb_robotState", Int8, queue_size=2)
	robot_status = data.data
	try:
		if robot_status == 3 and new_robot_status == 0:
			send_open_request(0)
			rospy.sleep(0.5)
			new_robot_status = 4
			pub.publish(new_robot_status)
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def send_reference_request():
	rospy.wait_for_service('/weiss_gripper_ieg76_driver/reference')
	try:
			reference = rospy.ServiceProxy('/weiss_gripper_ieg76_driver/reference', Trigger)
			resp = reference()
			if resp.success == True:
				print "Success: " + resp.message
			else:
				print "Failure: " + resp.message
	except rospy.ServiceException, e:
			print "Service call failed: %s"%e

def send_grasp_object_request(grasp_config_no):
	rospy.wait_for_service('/weiss_gripper_ieg76_driver/grasp')
	try:
			grasp_object = rospy.ServiceProxy('/weiss_gripper_ieg76_driver/grasp', Move)
			resp = grasp_object(grasp_config_no)
			if resp.success == True:
				print "Success: " + resp.message
			else:
				print "Failure: " + resp.message
	except rospy.ServiceException, e:
			print "Service call failed: %s"%e

def send_open_request(grasp_config_no):
	rospy.wait_for_service('/weiss_gripper_ieg76_driver/open')
	try:
			open_jaws = rospy.ServiceProxy('/weiss_gripper_ieg76_driver/open', Move)
			resp = open_jaws(grasp_config_no)
			if resp.success == True:
				print "Success: " + resp.message
			else:
				print "Failure: " + resp.message
	except rospy.ServiceException, e:
			print "Service call failed: %s"%e

if __name__ == "__main__":
	rospy.init_node('state_listener')
	rospy.Subscriber("bru_ctrl_state", Int8, state_callback)
	rospy.Subscriber("bru_irb_robotState", Int8, callback_robot_status)
	rospy.Subscriber("bru_irb_calibrationState", Int8, callback_calibration_status)
	grasp_config_no = 0
	rospy.spin()
