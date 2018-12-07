/*
NODE bru_vis_grayImg
Zet een kleur image om naar een grijswaarde image
- Subscribe op: /camera/color/image_raw
- Publish naar: /bru/vis/grayImg

Door: Giel Oomen; 2103640; Avans Breda
*/

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include "sensor_msgs/Image.h"
#include <sensor_msgs/image_encodings.h>

// Aanmaken globaal Mat object, zodat deze in de callback kan worden opgehaald
// en vervolgens in de node kan worden gebruikt
cv::Mat colorImgOCV;

void imageCallback(const sensor_msgs::ImageConstPtr& colorImg)
{
  // Maken en tonen OpenCV image
  colorImgOCV = cv_bridge::toCvShare(colorImg, "bgr8")->image;
}

int main(int argc, char **argv)
{
  // Initialiseren van de Nodehandle, Subscriber en Publisher
  // Nodenaam: bru_vis_grayImg
  // Subscribe op: /camera/color/image_raw
  // Publish naar: /bru/vis/grayImg
  ros::init(argc, argv, "bru_vis_grayImg");

  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("/camera/color/image_raw", 3, imageCallback);
  ros::Publisher pub = n.advertise<sensor_msgs::Image>("/bru/vis/grayImg", 3);

  // Loopen door de node, indien er een image is opgehaald uit de callback functie
  // wordt deze omgezet naar een
  while(ros::ok()){
      cv::Mat grayImg;
      //cv::imshow("color image", colorImgOCV);
      //cv::waitKey(30);

      if(colorImgOCV.cols > 0){
        cv::cvtColor(colorImgOCV, grayImg, CV_BGR2GRAY);
        //cv::imshow("gray image", grayImg);
        //cv::waitKey(30);
        cv_bridge::CvImage cv_image;
        cv_image.image = grayImg;
        cv_image.encoding = "mono8";
        sensor_msgs::Image test_image;
        cv_image.toImageMsg(test_image);
        pub.publish(test_image);
      }
      ros::spinOnce();
      ros::Rate loop_rate(10);
  }

  ros::spin();

  return 0;
}
