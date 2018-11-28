/*
NODE bru_vis_displayV2
Updated display node. Retrieves image, hole and depth data and combines these into one image.
- Subscribes to: /camera/color/image_raw
- Publishes to: /bru_vis_keypoints

By: Giel Oomen; 2103640; Avans Breda
*/

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include "sensor_msgs/Image.h"
#include "opencv2/core.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/objdetect.hpp"
#include "opencv2/features2d.hpp"
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include "vision/imageCircleData.h"
#include "vision/VectorData.h"

using namespace cv;
using namespace std;

cv::Mat colorImgOCV;
vector<KeyPoint> keypointVec;

void imageCallback(const sensor_msgs::ImageConstPtr& colorImg)
{
  // Converting ROS image to OpenCV image for recognition
  colorImgOCV = cv_bridge::toCvShare(colorImg, "bgr8")->image;
}

void holeDataCallback(const vision::imageCircleData circleData)
{
  // retrieve circledata and transfer these into a keypoint vector
  keypointVec.clear();
  

}

// Creating struct from custom message type
//::vision::VectorData XYSizeData;

int main(int argc, char **argv)
{
  // Initialisation of the Nodehandle, Subscriber en Publisher
  ros::init(argc, argv, "bru_vis_circledetection");

  ros::NodeHandle n;
  ros::Subscriber imageSub = n.subscribe("/camera/color/image_raw", 4, imageCallback);
  ros::Subscriber holeDataSub = n.subscribe("/bru_vis_holeData", 4, holeDataCallback);
  ros::Publisher pub = n.advertise<vision::imageCircleData>("/bru_vis_test", 4);

  // Main loop
  while(ros::ok()){


      ros::spinOnce();
      //ros::Rate loop_rate(10);

  }
  ros::spin();

  return 0;
}
