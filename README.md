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
1. Download de Arduino IDE (https://www.arduino.cc/en/Main/Software)

Als de .tar.xz file gedownload is pak deze uit in een map naar jouw keuze. E.g. $Home/arduino-1.8.7.

Voer de volgende commando's uit: 

- cd sketchbook

- ./install.sh

sketchbook moet vervangen worden met de huidige versie van arduino. E.g. cd arduino-1.8.7. Het meegegeven pad aan de cd commando is afhankelijk van waar de tar-file is uitgepakt.

2. Voer de volgende commando's uit:

- sudo apt-get install ros-indigo-rosserial-arduino

- sudo apt-get install ros-indigo-rosserial

Deze commando's zorgen ervoor dat de rosserial wordt geinstalleerd op het ROS werkstation. Vervang indigo met de huidige ROS versie.

3. Voer de volgende commando's uit: 

- cd sketchbook/libraries 
  
- rm -rf ros_lib

- rosrun rosserial_arduino make_libraries.py .

Vervang sketchbook door huidige Arduino versie E.g. cd arduino-1.8.7/libraries

#### Intel RealSense Driver
