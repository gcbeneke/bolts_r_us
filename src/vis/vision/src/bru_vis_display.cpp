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

// Aanmaken globaal Mat objecten, zodat deze in de callback kunnen worden opgehaald
// en vervolgens in de node kan worden gebruikt
cv::Mat colorImgOCV;
cv::Mat grayImgOCV;
cv::Mat threshImgOCV;
cv::Mat threshImg;
// Color image callback
void colorImageCallback(const sensor_msgs::ImageConstPtr& colorImg)
{
  // Omzetten naar OpenCV image
  colorImgOCV = cv_bridge::toCvShare(colorImg, "bgr8")->image;
}

// Gray Image Callback
void grayImageCallback(const sensor_msgs::ImageConstPtr& grayImg)
{
  // Omzetten naar OpenCV image
  grayImgOCV = cv_bridge::toCvShare(grayImg, "mono8")->image;
}

// Threshold Image Callback

void threshImageCallback(const sensor_msgs::ImageConstPtr& threshImg)
{
  // Omzetten naar OpenCV image
  threshImgOCV = cv_bridge::toCvShare(threshImg, "bgr8")->image;
}

int main(int argc, char **argv)
{
  // Initialiseren van de Nodehandle, Subscribers en Publisher
  ros::init(argc, argv, "bru_vis_display");

  ros::NodeHandle n;
  ros::Subscriber graySub = n.subscribe("/bru/vis/grayImg", 5, grayImageCallback);
  ros::Subscriber colorSub = n.subscribe("/camera/color/image_raw", 4, colorImageCallback);

  //ros::Subscriber threshSub = n.subscribe("/bru/vis/threshImg", 4, threshImageCallback);

  int alpha_slider;
  cv::Mat tijdelijk;
  // Loopen door de node, indien er een image is opgehaald uit de callback functie
  // wordt deze omgezet naar een
  while(ros::ok()){
      //cv::imshow("color image", colorImgOCV);
      //cv::waitKey(30);

      if(grayImgOCV.empty() == false){
        cv::imshow("gray image", grayImgOCV);
        cv::waitKey(30);
        grayImgOCV.copyTo(threshImg);

        // Controleren of er data in de image staat om te kunnen thresholden
        if(threshImg.empty() == false){
          cv::createTrackbar( "Threshold", "Trackbar test", &alpha_slider, 255);

          cv::threshold( grayImgOCV, threshImg, alpha_slider, 255, cv::THRESH_BINARY_INV);
          ros:sleep(0.1);
          tijdelijk = threshImg;
          if(tijdelijk.empty() == false){
            cv::imshow("Trackbar test", tijdelijk);
            cv::waitKey(30);
          }

        }
      }
      ros::spinOnce();
      ros::Rate loop_rate(10);
  }

  ros::spin();

  return 0;
}
