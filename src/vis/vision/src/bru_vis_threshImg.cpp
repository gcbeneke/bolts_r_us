/*
NODE bru_vis_threshImg
Zet een kleur image om naar een grijswaarde image
- Subscribe op: /bru/vis/grayImg
- Publish naar: /bru/vis/threshImg

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
cv::Mat grayImgOCV;
cv::Mat threshImg;

void grayImageCallback(const sensor_msgs::ImageConstPtr& grayImg)
{
  // Maken en tonen OpenCV image
  grayImgOCV = cv_bridge::toCvShare(grayImg, "mono8")->image;
}

int main(int argc, char **argv)
{
  // Initialiseren van de Nodehandle, Subscriber en Publisher
  // Nodenaam: bru_vis_threshImg
  // Subscribe op: /bru/vis/grayImg
  // Publish naar: /bru/vis/threshImg
  ros::init(argc, argv, "bru_vis_threshImg");

  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("bru/vis/grayImg", 5, grayImageCallback);
  ros::Publisher pub = n.advertise<sensor_msgs::Image>("/bru/vis/threshImg", 3);

  int alpha_slider;
  cv::Mat tijdelijk;
  // Loopen door de node, indien er een image is opgehaald uit de callback functie
  // wordt deze omgezet naar een thresh image
  while(ros::ok()){
      // Controleren of er data in de gray image staat
      if(grayImgOCV.empty() == false){
        cv::imshow("gray image", grayImgOCV);
        cv::waitKey(30);
        threshImg = grayImgOCV;

        // Controleren of er data in de image staat om te kunnen thresholden
        if(threshImg.empty() == false){
          cv::createTrackbar( "Threshold", "Trackbar test", &alpha_slider, 255);

          cv::threshold( grayImgOCV, threshImg, alpha_slider, 255, cv::THRESH_BINARY_INV);
          tijdelijk = threshImg;
          if(tijdelijk.empty() == false){
            cv::imshow("Trackbar test", tijdelijk);
            cv::waitKey(30);
          }

        }


        /*
        cv_bridge::CvImage cv_image;
        cv_image.image = grayImg;
        cv_image.encoding = "mono8";
        sensor_msgs::Image test_image;
        cv_image.toImageMsg(test_image);
        pub.publish(test_image);
        */
      }

      ros::spinOnce();
      ros::Rate loop_rate(10);
  }
  cv::destroyAllWindows();

  return 0;
}
