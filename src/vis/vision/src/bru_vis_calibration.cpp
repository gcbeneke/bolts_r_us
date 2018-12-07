/*
NODE bru_vis_display
Haalt verschillende images op en biedt de mogelijkheid om deze weer te geven
- Subscribe op: /camera/color/image_raw
- Subscribe op: /bru/vis/grayImg
- Subscribe op: /bru/vis/threshImg
- Publish naar: /bru/vis/threshold

Door: Giel Oomen; 2103640; Avans Breda
*/

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include "sensor_msgs/Image.h"

// Create global Mat object to use in main
cv::Mat colorImgOCV;

// Color image callback
void colorImageCallback(const sensor_msgs::ImageConstPtr& colorImg)
{
  // Converts ROS image to OpenCV image type
  colorImgOCV = cv_bridge::toCvShare(colorImg, "bgr8")->image;
}



int main(int argc, char **argv)
{
  // Initialisation of nohandle and subscribers
  ros::init(argc, argv, "bru_vis_display");

  ros::NodeHandle n;
  ros::Subscriber colorSub = n.subscribe("/camera/color/image_raw", 4, colorImageCallback);


  while(ros::ok()){

    ros::spinOnce();
    ros::Rate loop_rate(10);
  }

  ros::spin();

  return 0;
}
