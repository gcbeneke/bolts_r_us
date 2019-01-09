/*
NODE bru_vis_displayV2
Updated display node. Retrieves image, hole and depth data and combines these into one image.
- Subscribes to: /camera/color/image_raw
- Subscribes to: /camera/color/holeData

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
vector<float> depth;
void imageCallback(const sensor_msgs::ImageConstPtr& colorImg)
{
  // Converting ROS image to OpenCV image for recognition
  colorImgOCV = cv_bridge::toCvShare(colorImg, "bgr8")->image;
}

void holeDataCallback(const vision::imageCircleData circleData)
{
  // retrieve circledata and transfer these into a keypoint vector
  KeyPoint singleKP;    // Variable that stores a single point
  keypointVec.clear();
  depth.clear();
  if(circleData.allHolesDataVec.empty() == false){
    for(int i = 0; i < circleData.allHolesDataVec.size(); i++){
      singleKP.pt.x = circleData.allHolesDataVec[i].x;
      singleKP.pt.y = circleData.allHolesDataVec[i].y;
      singleKP.size = circleData.allHolesDataVec[i].size;
      depth.push_back(circleData.allHolesDataVec[i].z);

      keypointVec.push_back(singleKP);

    }
  }
  else{
    std::cout << "No circledata retrieved from topic!" << '\n';
  }
}

// Creating struct from custom message type
//::vision::VectorData XYSizeData;

int main(int argc, char **argv)
{
  // Initialisation of the Nodehandle, Subscriber en Publisher
  ros::init(argc, argv, "bru_vis_displayV2");

  ros::NodeHandle n;
  ros::Subscriber imageSub = n.subscribe("/camera/color/image_raw", 4, imageCallback);
  ros::Subscriber holeDataSub = n.subscribe("/bru_vis_holeData", 4, holeDataCallback);
  //ros::Publisher pub = n.advertise<vision::imageCircleData>("/bru_vis_test", 4);

  // Main loop
  while(ros::ok()){

    Mat im_with_keypoints;
    if (colorImgOCV.empty() == false){
      // Draw the circles in the current frame
      drawKeypoints(colorImgOCV, keypointVec, im_with_keypoints, Scalar(0, 0, 255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS);

      // Write the information next to each circle
      for(int i = 0; i < keypointVec.size(); i++){
        // Add Circle number to image
        putText(im_with_keypoints, "Circle: "+ to_string(i), cvPoint(keypointVec[i].pt.x + 10,keypointVec[i].pt.y + (keypointVec[i].size/2)),
        FONT_HERSHEY_DUPLEX, 0.5, cvScalar(0,0,255), 1, CV_AA);

        // Add Circle distance to image
        putText(im_with_keypoints, "Depth "+ to_string(depth[i]), cvPoint(keypointVec[i].pt.x + 10,keypointVec[i].pt.y +15 + (keypointVec[i].size/2)),
        FONT_HERSHEY_DUPLEX, 0.5, cvScalar(0,0,255), 1, CV_AA);
      }
      imshow("Videostream met diepte", im_with_keypoints);
      waitKey(30);


    }


    ros::spinOnce();
    //ros::Rate loop_rate(10);

  }
  ros::spin();

  return 0;
}
