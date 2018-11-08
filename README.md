# Minor Vision & Robotics Project 11
### Bolts R Us

Dit is de Readme file voor het project Bolts R Us. De gehele source code is gemaakt in C++ en gebruikt ROS als middleware voor 
het overbrengen van data.

##

### Contents
  - Installatie voorwaarden
  - How to install
  - Starten van het systeem
  
##
  
### Installatie voorwaarden
Voor het runnen van de software zijn verschillende drivers en packages nodig van Optoforce, ABB en Intel RealSense. Hieronder 
staan de verschillende drivers die nodig zijn met bijbehorende URL's om deze te downloaden.

#### Arduino Driver
Hieronder staat een link voor het installeren van de rosserial voor Arduino IDE. Rosserial wordt gebruikt om de knoppen uit te lezen.
http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup

Hieronder volgt ook een korte omschrijving van de stappen:
1. Download & installeer de Arduino IDE (https://www.arduino.cc/en/Main/Software)
Volg hierbij de instructies van de installer.

2. Voer de volgende commandos uit: 
sudo apt-get install ros-indigo-rosserial-arduino
sudo apt-get install ros-indigo-rosserial

Deze commandos zorgen ervoor dat de rosserial wordt geinstalleerd op het ROS werkstation. Vervang indigo met de huidige ROS versie

3. Voer de volgende commando's uit: 

cd <sketchbook>/libraries 
rm -rf ros_lib
rosrun rosserial_arduino make_libraries.py .

(<sketchbook> vervangen door huidige Arduino versie E.g. cd arduino-1.8.7/libraries)

#### Intel RealSense Driver
