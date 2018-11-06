#include "ros/ros.h"
#include "std_msgs/String.h"
#include "ctrl/State.h"

int buttonState;

int main(int argc, char **argv){
  ros::init(argc, argv, "statePub");
  ros::NodeHandle n;

  ros::Publisher state_pub = n.advertise<ctrl::State>("bru_ctrl_state", 1000);
  ros::Rate loop_rate(10);

  while(ros::ok){
    ctrl::State msg;
    bool startButton, stopButton, caliButton;
    if(startButton == true){
      msg.state = 1;
    } else if (stopButton == true){
      msg.state = 2;
    } else if (caliButton == true){
      msg.state = 3;
    }
    state_pub.publish(msg);
  }
}
