#include "ros/ros.h"
#include "std_msgs/String.h"
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>

int buttonState;

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv){
  ros::init(argc, argv, "realSenseListener");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("/camera/color/image_raw", 1000, chatterCallback);
  ros::spin();

  return 0;

}
