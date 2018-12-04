/*
NODE bru_vis_circleDetection
Collects the raw images coming from the Intel Realsense camera and processes these to hole data
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

void imageCallback(const sensor_msgs::ImageConstPtr& colorImg)
{
  // Converting ROS image to OpenCV image for recognition
  colorImgOCV = cv_bridge::toCvShare(colorImg, "bgr8")->image;
}

// Creating struct from custom message type
::vision::VectorData XYSizeData;


int main(int argc, char **argv)
{
  // Initialisation of the Nodehandle, Subscriber en Publisher
  ros::init(argc, argv, "bru_vis_circledetection");

  ros::NodeHandle n;
  ros::Subscriber colorSub = n.subscribe("/camera/color/image_raw", 4, imageCallback);
  ros::Publisher pub = n.advertise<vision::imageCircleData>("/bru_vis_holeData", 4);

  // Main loop
  while(ros::ok()){

      // Detect blobs.
      std::vector<KeyPoint> keypoints;
      ::vision::imageCircleData allHoles;
      // DrawMatchesFlags::DRAW_RICH_KEYPOINTS flag ensures the size of the circle corresponds to the size of blob
      Mat im_with_keypoints;

      // Setup SimpleBlobDetector parameters.
      SimpleBlobDetector::Params params;

      // Change thresholds
      params.minThreshold = 10;
      params.maxThreshold = 220;

      // Filter by Area.
      params.filterByArea = true;
      params.minArea = 40;

      // Filter by Circularity
      params.filterByCircularity = true;
      params.minCircularity = 0.7;

      // Filter by Convexity
      params.filterByConvexity = false;
      params.minConvexity = 0.87;

      // Filter by Inertia
      params.filterByInertia = false;
      params.minInertiaRatio = 0.01;

      // Set up detector with params
      Ptr<SimpleBlobDetector> detector = SimpleBlobDetector::create(params);

      if (colorImgOCV.empty() == false){
        //SimpleBlobDetector::create creates a smart pointer.
        // So you need to use arrow ( ->) instead of dot ( . )
        detector->detect(colorImgOCV, keypoints);

        // Every hole found is added to vector allHolesDataVec
        for(int i = 0; i < keypoints.size(); i++){
          XYSizeData.x = keypoints[i].pt.x;
          XYSizeData.y = keypoints[i].pt.y;
          XYSizeData.size = keypoints[i].size;
          allHoles.vector_name = "Data_of_all_holes";
          allHoles.allHolesDataVec.push_back(XYSizeData);
        }

        // Check if there are holes found, if there are -> publish values to topic
        if(allHoles.allHolesDataVec.empty() == false){
          std::cout << "Publishing values" << '\n';
          pub.publish(allHoles);
        }

        // UNCOMMENT THIS BLOCK FOR VIDEO FEEDBACK
        /*
        drawKeypoints(colorImgOCV, keypoints, im_with_keypoints, Scalar(0, 0, 255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
        imshow("Videostream", im_with_keypoints);
        waitKey(30);
        */
        // END OF VIDEOSTREAM

      } else{
        std::cout << "No image found from the Intel Realsense camera" << '\n';
      }

      ros::spinOnce();
      //ros::Rate loop_rate(10);

  }
  ros::spin();

  return 0;
}
