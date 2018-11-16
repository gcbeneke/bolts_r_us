
#include "ros/ros.h"
#include <stdlib.h>
#include <stdio.h>
#include "std_msgs/Bool.h"
#include "geometry_msgs/WrenchStamped.h"
#include "opt/OptoForceData.h"

ros::Time lastTime(0);
ros::Time overallTime(0);
unsigned int packetCount = 0;
ros::Duration accDuration(0);

float fx, fy, fz;
float tx, ty, tz;

void chatterCallback(const geometry_msgs::WrenchStamped& msg)
{
	ros::Time currentTime(ros::Time::now());

	if (lastTime == ros::Time(0)) {
		lastTime = currentTime;
	}
	if (overallTime.isZero()) {
		overallTime = currentTime;
	}
	ros::Duration duration = currentTime - lastTime;
	accDuration += duration;
	double durationTime = duration.toSec() * 1000.0;
	double frequency = 0.0;
	++packetCount;
	if (accDuration.toSec() > 1.0) {
		accDuration = ros::Duration(0);
		packetCount = 0;
	}

	if (accDuration.isZero() == false) {
		frequency = (double)packetCount / accDuration.toSec();
	}

	lastTime = currentTime;

	fx = msg.wrench.force.x, fy = msg.wrench.force.y, fz = msg.wrench.force.z;
	tx = msg.wrench.torque.x, ty = msg.wrench.torque.z, tz = msg.wrench.torque.z;
}

int main (int argc, char ** argv)
{
	int speed = 0;
	ros::init(argc, argv, "bru_opt_publisher");
	ros::NodeHandle n;
	ros::Rate loop_rate(1000);  // The loop rate
	ros::Publisher zero_pub = n.advertise<std_msgs::Bool>("ethdaq_zero", 1);  // The topic where we send "zeroing" (Like tare)
	ros::Subscriber sub_raw = n.subscribe("ethdaq_data_raw", 1000, chatterCallback); // The callback where we waiting for Wrench data
	ros::Subscriber sub_new = n.subscribe("ethdaq_data", 1000, chatterCallback);
	ros::Publisher workData = n.advertise<opt::OptoForceData>("bru_opt_workData", 1);


	ros::Duration zeroingTime(10.0);
	ros::Time lastZeroing = ros::Time::now();
	bool zeroing = true;
	while (ros::ok()) {
		ros::spinOnce();
		loop_rate.sleep();
		speed++;
		opt::OptoForceData ft;
		ft.fx = fx;
		ft.fy = fy;
		ft.fz = fz;
		ft.tx = tx;
		ft.ty = ty;
		ft.tz = tz;
		workData.publish(ft);

		if (lastTime.isZero()) {
			continue;
		}
		ros::Time currentTime = ros::Time::now();
		if (currentTime - lastZeroing >= zeroingTime) {
			// We do a zeroing/unzeroing in every 10 secs

			std_msgs::Bool z;
			z.data = zeroing;
			zero_pub.publish(z);
			zeroing = !zeroing;
			lastZeroing = currentTime;
		}
	}

	return 0;
}
