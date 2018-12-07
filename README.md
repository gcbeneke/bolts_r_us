# Minor Vision & Robotics Project 11
### Bolts R Us

Calibratie camera: https://trojan03.github.io/#!/blog/4

Dit is de Readme file voor het project Bolts R Us. De gehele source code is gemaakt in C++ en in Python en gebruikt ROS als middleware voor 
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

##

#### Arduino Driver
Hieronder staat een link voor het installeren van de rosserial voor Arduino IDE. Rosserial wordt gebruikt om de knoppen uit te lezen.
http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup

Hieronder volgt ook een korte omschrijving van de stappen:
1. Download de Arduino IDE (https://www.arduino.cc/en/Main/Software)

Als de .tar.xz file gedownload is pak deze uit in een map naar jouw keuze. E.g. $Home/arduino-1.8.7.

Voer de volgende commando's uit: 

- `cd sketchbook`

- `./install.sh`

sketchbook moet vervangen worden met de huidige versie van arduino. E.g. cd arduino-1.8.7. Het meegegeven pad aan de cd commando is afhankelijk van waar de tar-file is uitgepakt.

2. Voer de volgende commando's uit:

- `cd ..`

- `sudo apt-get install ros-indigo-rosserial-arduino`

- `sudo apt-get install ros-indigo-rosserial`

Deze commando's zorgen ervoor dat de rosserial wordt geinstalleerd op het ROS werkstation. Vervang indigo met de huidige ROS versie.

3. Voer de volgende commando's uit: 

- `cd sketchbook/libraries`
  
- `rm -rf ros_lib`

- `rosrun rosserial_arduino make_libraries.py`

Vervang sketchbook door huidige Arduino versie E.g. cd arduino-1.8.7/libraries

##

#### Intel RealSense Driver & Packages
Om gebruik te kunnen maken van de Intel RealSense D435 module is de driver nodig en er wordt een package gedownload om de werking te controleren. Daarnaast werkt de driver alleen op Linux kernals versie **4.16**

**Controleer de huidige kernel versie met de volgende command:**
  `uname -r`

**Als deze versie niet gelijk is aan 4.16 moet eerst een nieuwe kernel worden geinstalleerd met de volgende tutorial:**
Volg het stukje bij 64-Bit OS op de pagina van onderstaande URL en start daarna opnieuw het systeem op. Tijdens het opstarten moet de optie **Advanced options for Linux** worden aangeklikt en hierbij kan de nieuwe kernel (4.16) worden gebruikt.

http://ubuntuhandbook.org/index.php/2018/04/install-kernel-4-16-ubuntu-linux-mint/


- librealsense2 **driver** installatie:

https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md

- realsense2_camera **package** installatie:

https://github.com/intel-ros/realsense/#installation-instructions

  
Deze versie moet **4.16+** zijn om zeker te weten dat het werkt.
  
Indien de huidige kernel versie niet werkt kan eerst de pc opnieuw worden opgestart en daarbij moet in het opstartmenu **Advanced Ubuntu options** daar kan de kernelversie worden gewijzigd.

##

#### ABB IRB120

Voor de connectie met de robot moeten er meerdere packages gedownload worden:

ROS industrial core ( https://github.com/ros-industrial/industrial_core )

ABB ( https://github.com/ros-industrial/abb.git )

ABB Experimental ( https://github.com/ros-industrial/abb_experimental.git )

Voer de catkin_make command uit

Als die lukt kan er verbinding gemaakt worden met de robot

Gun de volgende launch file: 

roslaunch abb_irb120_support robot_interface_download_irb120_3_58.launch robot_ip:=<IP_OF_YOUR_ROBOT>
En vervang IP_OF_YOUR_ROBOT door het ipadres van de robot

Als dit lukt moet er op de flexpendant van de robot staan die hij geconnected is. 


Mocht de robot niet goed openen in de simulatie (Rviz)

Run dan de volgende command voordat je de simulatie runt:

`export LC_NUMERIC="en_US.UTF-8"` 

TIP:

Zet het command in de ~/.bashrc file zodat elke keer als de terminal wordt geopend het goed ingesteld is.
