#!/usr/bin/env python
import roslib;
import sys
import rospy
import math
from std_srvs.srv import Trigger
from weiss_gripper_ieg76.srv import *
from std_msgs.msg import Int8

def state_callback(msg):
	status = msg.data
	try:
			if status == 1:
				#print "Success: "
				send_reference_request()
				send_open_request(16)

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
	grasp_config_no = 0
	rospy.spin()
