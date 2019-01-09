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
#include "sensor_msgs/PointCloud2.h"
#include "sensor_msgs/point_cloud_conversion.h"
#include "vision/imageCircleData.h"
#include "vision/VectorData.h"

#include "opencv2/core.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/objdetect.hpp"
#include "opencv2/features2d.hpp"
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <vector>
#include <iostream>


using namespace cv;
using namespace std;

// Global variables to use in callbacks and main functions.
cv::Mat colorImgOCV;
sensor_msgs::PointCloud convertedPC;
::vision::VectorData XYZSizeData;
int pcHeight;
int pcWidth;
double offSet;


void imageCallback(const sensor_msgs::ImageConstPtr& colorImg)
{
  // Converting ROS image to OpenCV image for recognition
  colorImgOCV = cv_bridge::toCvShare(colorImg, "bgr8")->image;
}


void depthCallback(const sensor_msgs::PointCloud2 raw_pc2)
{
  sensor_msgs::convertPointCloud2ToPointCloud(raw_pc2, convertedPC);
  pcHeight = raw_pc2.height;
  pcWidth = raw_pc2.width;
}

// Function to check the depth of all found circles. It has to be within the specified range.
int checkDepth(const sensor_msgs::PointCloud inputCloud, const vector<KeyPoint> keypoints, ::vision::imageCircleData &allHoles){
  if(inputCloud.points.size() == 0){
    std::cout << "No PointCloud2 data coming from Intel Realsense, can't filter!" << '\n';
    return 1;
  }

  // Check depth of each circle, if the depth differs from the given range then don't publish keep the data
  for(int i = 0; i < keypoints.size(); i++){
    XYZSizeData.x = keypoints[i].pt.x;
    XYZSizeData.y = keypoints[i].pt.y;
    XYZSizeData.z = inputCloud.points[XYZSizeData.x * XYZSizeData.y].z;
    XYZSizeData.size = keypoints[i].size;

    offSet = sqrt(XYZSizeData.size/3.14);
    XYZSizeData.x = XYZSizeData.x + offSet;

    //if(XYZSizeData.z > 0.25 && XYZSizeData.z < 0.5){
    allHoles.allHolesDataVec.push_back(XYZSizeData);
    //}
  }
}


int main(int argc, char **argv)
{
  // Initialisation of the Nodehandle, Subscriber en Publisher
  ros::init(argc, argv, "bru_vis_circledetection");

  ros::NodeHandle n;
  ros::Subscriber colorSub = n.subscribe("/camera/color/image_raw", 4, imageCallback);
  ros::Subscriber depthSub = n.subscribe("/camera/depth/color/points", 4, depthCallback);
  ros::Publisher pub = n.advertise<vision::imageCircleData>("/bru_vis_holeData", 4);

  int alpha_slider;
  int beta_slider;

  // Setup SimpleBlobDetector parameters.
  SimpleBlobDetector::Params params;

  //filter by colour
  //params.filterByColor=false;
  //params.blobColor=180;

  // Change thresholds
  params.minThreshold = 36;
  params.maxThreshold = 255;

  // Filter by Area.
  params.filterByArea = true;
  params.minArea = 100;

  // Filter by Circularity
  params.filterByCircularity = true;
  params.minCircularity = 0.75;

  // Filter by Convexity
  params.filterByConvexity = false;
  params.minConvexity = 0.87;

  // Filter by Inertia
  params.filterByInertia = false;
  params.minInertiaRatio = 0.01;

  // Set up detector with params
  Ptr<SimpleBlobDetector> detector = SimpleBlobDetector::create(params);
  Mat im_with_keypoints;



  // Main loop
  while(ros::ok()){

      // Detect blobs.
      std::vector<KeyPoint> keypoints;
      ::vision::imageCircleData allHoles;
      // DrawMatchesFlags::DRAW_RICH_KEYPOINTS flag ensures the size of the circle corresponds to the size of blob


      if (colorImgOCV.empty() == false){
        //SimpleBlobDetector::create creates a smart pointer.
        // So you need to use arrow ( ->) instead of dot ( . )
        detector->detect(colorImgOCV, keypoints);

        // Use the converted pointcloud and keypoints to save the right holes in a vector with X, Y, Z and Size data
        checkDepth(convertedPC, keypoints, allHoles);

        // Check if there are holes found, if there are -> publish values to topic
        if(allHoles.allHolesDataVec.empty() == false){
          std::cout << "Publishing values" << '\n';
          pub.publish(allHoles);
        }


        // UNCOMMENT THIS BLOCK FOR VIDEO FEEDBACK
        drawKeypoints(colorImgOCV, keypoints, im_with_keypoints, Scalar(0, 0, 255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
        imshow("Videostream_circledata", im_with_keypoints);
        waitKey(30);

        // END OF VIDEOSTREAM
        Mat grayImgOCV = colorImgOCV;

        Mat threshImg;
        cvtColor(colorImgOCV, grayImgOCV, CV_BGR2GRAY);
        if(grayImgOCV.empty() == false){
          //cv::imshow("gray image", grayImgOCV);
          //cv::waitKey(30);
          //Mat threshImg = grayImgOCV;

          // Controleren of er data in de image staat om te kunnen thresholden
          cv::createTrackbar( "Threshold_min", "Threshold_set", &alpha_slider, 255);
          cv::createTrackbar( "Threshold_max", "Threshold_set", &beta_slider, 255);

          cv::threshold( grayImgOCV, threshImg, alpha_slider, beta_slider, cv::THRESH_BINARY);
          Mat tijdelijk = threshImg;
          if(tijdelijk.empty() == false){
            cv::imshow("Threshold_set", tijdelijk);
            cv::waitKey(30);
          }

          }

      } else{
        std::cout << "No image found from the Intel Realsense camera" << '\n';
      }

      ros::spinOnce();
      ros::Rate loop_rate(33);

  }
  ros::spin();

  return 0;
}
