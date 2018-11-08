#include "ros/ros.h"
#include "std_msgs/String.h"
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>

int buttonState;

int main(int argc, char **argv){
  ros::init(argc, argv, "colorCameraPub");
  ros::NodeHandle nh;

  image_transport::ImageTransport it(nh);

  image_transport::Publisher pub = it.advertise("bru_vis_colorImg", 1);

  cv::VideoCapture cap(1);
  // Check if video device can be opened with the given index
  if(!cap.isOpened()) return 1;
  cv::Mat frame;
  sensor_msgs::ImagePtr msg;

  ros::Rate loop_rate(5);
  while (nh.ok()) {
    cap >> frame;
    // Check if grabbed frame is actually full with some content
    if(!frame.empty()) {
      msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
      pub.publish(msg);
      cv::waitKey(1);
    }

    ros::spinOnce();
    loop_rate.sleep();
  }

}
