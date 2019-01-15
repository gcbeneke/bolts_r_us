#include "ros/ros.h"
#include <stdlib.h>
#include <stdio.h>
#include "std_msgs/Bool.h"
#include "geometry_msgs/WrenchStamped.h"
#include "opt/Corrections.h"
#include "opt/OptoForceData.h"

float fx, fy, fz;
float tx, ty, tz;
const int MAX_SIZE = 6;
float corrections[MAX_SIZE] = {};

// ophalen optoforce data
void chatterCallback(const opt::OptoForceData& msg)
{
	fx = msg.fx;
  fy = msg.fy;
  fz = msg.fz;
  tx = msg.tx;
  ty = msg.ty;
  tz = msg.tz;
}

int main (int argc, char ** argv)
{
	bool zeroing;

  float lastFx, lastFy, lastFz;
  float lastTx, lastTy, lastTz;

  float newFx, newFy, newFz;
  float newTx, newTy, newTz;

  float offSet_Fx, offSet_Fy, offSet_Fz;
  float offSet_Tx, offSet_Ty, offSet_Tz;

	float avg_offSet_Fx, avg_offSet_Fy, avg_offSet_Fz;
	float avg_offSet_Tx, avg_offSet_Ty, avg_offSet_Tz;

	int i = 0;

	ros::init(argc, argv, "bru_irb_placeBolt");
  ros::NodeHandle n;
  ros::Rate loop_rate(1000);
  ros::Subscriber sub_opt_workData = n.subscribe("bru_opt_workData", 1000, chatterCallback);
  ros::Publisher pub_correctPos = n.advertise<opt::Corrections>("bru_new_force", 1);
	ros::Publisher pub_avg_offset = n.advertise<opt::Corrections>("bru_avg_offset", 1);

  while(ros::ok){

		newFx = fx, newFy = fy, newFz = fz;
		newTx = tx, newTy = ty, newTz = ty;

    ros::spinOnce();
		loop_rate.sleep();

		// data verwerken naar gemiddelde offset
		if(i < 100){
			offSet_Fx += newFx-lastFx;
			offSet_Fy += newFy-lastFy;
			offSet_Fz += newFz-lastFz;
			offSet_Tx += newTx-lastTx;
			offSet_Ty += newTy-lastTy;
			offSet_Tz += newTz-lastTz;
		}

		opt::Corrections pub;
		opt::Corrections avg;

		// gemiddelde offset berekenen
		if(i > 99){
			avg_offSet_Fx = offSet_Fx/i;
			avg_offSet_Fy = offSet_Fy/i;
			avg_offSet_Fz = offSet_Fz/i;
			avg_offSet_Tx = offSet_Tx/i;
			avg_offSet_Ty = offSet_Ty/i;
			avg_offSet_Tz = offSet_Tz/i;

			i = 0;

			avg.offSet[0] = avg_offSet_Fx;
			avg.offSet[1] = avg_offSet_Fy;
			avg.offSet[2] = avg_offSet_Fz;
			avg.offSet[3] = avg_offSet_Tx;
			avg.offSet[4] = avg_offSet_Ty;
			avg.offSet[5] = avg_offSet_Tz;

			// offset publiceren
	    pub.offSet[0] = newFx;
			pub.offSet[1] = newFy;
			pub.offSet[2] = newFz;
			pub.offSet[3] = newTx;
			pub.offSet[4] = newTy;
			pub.offSet[5] = newTz;
			pub_avg_offset.publish(avg);
			pub_correctPos.publish(pub);

			// alles naar nul brengen
			offSet_Fx = 0;
			offSet_Fy = 0;
			offSet_Fz = 0;
			offSet_Tx = 0;
			offSet_Ty = 0;
			offSet_Tz = 0;
		}

		// alles naar nul brengen
		for(int i = 0; i < MAX_SIZE; i++){
			avg.offSet[i]=0;
		}

		// nieuwe data is oude data
		lastFx = newFx, lastFy = newFy, lastFz = newFz;
		lastTx = newTx, lastTy = newTy, lastTz = newTz;
		i++;
  }
  return 0;
}
