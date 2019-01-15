/*
 * Button Example for Rosserial
 */

#include <ros.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Int8.h>

ros::NodeHandle nh;

std_msgs::Int8 state_msg;
ros::Publisher buttonState("bru_ctrl_state", &state_msg);

const int startButton = 3;
const int stopButton = 4;
const int caliButton = 2;

int state = 0;
bool published = false;
bool publishedStop = false;
bool publishedCali = false;

void setup()
{
  nh.initNode();
  nh.advertise(buttonState);

  //initialize an LED output pin
  //and a input pin for our push button
  pinMode(startButton, INPUT);
  pinMode(stopButton, INPUT);
  pinMode(caliButton, INPUT);

  //Enable the pullup resistor on the button
  digitalWrite(startButton, HIGH);
  digitalWrite(stopButton, HIGH);
  digitalWrite(caliButton, HIGH);

  //The button is a normally button
  //last_reading = ! digitalRead(button_pin);

}

void loop()
{
  bool startB = digitalRead(startButton);
  bool stopB = digitalRead(stopButton);
  bool caliB = digitalRead(caliButton);
  // Checks which state the button is in
  // Three options, start, stop and calibrate
  if (startB == false && state != 1 && published != true){
    state = 1;
    published = true;
    publishedStop = false;
    publishedCali = false;
    //Serial.print(state);
    Serial.println(". Started");
  }
  else if (stopB == false && state != 2 && publishedStop != true){
    state = 2;
    published = false;
    publishedStop = true;
    publishedCali = false;
    //Serial.print(state);
    Serial.println(". Stopped");
  }
    else if (caliB == false && publishedCali != true && state != 3){
    state = 3;
    published = false;
    publishedStop = false;
    publishedCali = true;
    //Serial.print(state);
    Serial.println(". Calibration");
  }

  if(state != 0){
    state_msg.data = state;
    Serial.println(state);
    buttonState.publish(&state_msg);
    state = 0;
  }
  // Delay of 100 ms
  delay(100);
  nh.spinOnce();
}
