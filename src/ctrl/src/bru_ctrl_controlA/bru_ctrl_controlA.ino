/* 
 * Button Example for Rosserial
 */

#include <ros.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Int8.h>

ros::NodeHandle nh;

std_msgs::Int8 state_msg;
ros::Publisher buttonState("bru_ctrl_state", &state_msg);

const int startButton = 2;
const int stopButton = 4;
const int caliButton = 8;

bool last_reading;
long last_debounce_time=0;
long debounce_delay=50;
bool published = true;

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
  //digitalWrite(button_pin, HIGH);
  
  //The button is a normally button
  //last_reading = ! digitalRead(button_pin);
 
}

void loop()
{
  int state;
  bool startB = digitalRead(startButton);
  bool stopB = digitalRead(stopButton);
  bool caliB = digitalRead(caliButton);
  
  if (startB == true){
    Serial.println("Startbutton pressed");
    startB = true;
    stopB = false;
    caliB = false;
    state = 1;
  } else if (stopB == true){
    Serial.println("Stopbutton pressed");
    startB = false;
    stopB = true;
    caliB = false;
    state = 2;
  } else if (caliB == true){
    Serial.println("Calibratebutton pressed");
    startB = false;
    stopB = false;
    caliB = true;
    state = 3;
  } else {
    state = 0;
  }

  if(state != 0){
    state_msg.data = state;
    buttonState.publish(&state_msg);
  }
  
  nh.spinOnce();
}
