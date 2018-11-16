cmake_minimum_required(VERSION 2.8.3)
project(opt)

find_package(catkin REQUIRED COMPONENTS
  cmake_modules
  diagnostic_msgs
  diagnostic_updater
  geometry_msgs
  roscpp
  message_generation
  actionlib_msgs
  std_msgs
)

find_package(Boost REQUIRED COMPONENTS system thread program_options)
find_package(CURL REQUIRED)
find_package(TinyXML REQUIRED)

add_message_files(
   FILES
   OptoForceData.msg
   Corrections.msg
)

#add_action_files(
#  FILES
#  Bru_irb_correctPosition.action
#  Bru_irb_rotateBolt.action
#)

generate_messages(
    DEPENDENCIES
    geometry_msgs
    std_msgs
    actionlib_msgs
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES etherdaq_driver
  CATKIN_DEPENDS diagnostic_msgs diagnostic_updater geometry_msgs roscpp
  CATKIN_DEPENDS message_runtime
  CATKIN_DEPENDS actionlib_msgs
)

include_directories(
 include ${catkin_INCLUDE_DIRS}
)

## Declare a cpp library
add_library(etherdaq_driver src/etherdaq_driver.cpp)
target_link_libraries(etherdaq_driver
  ${catkin_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CURL_LIBRARIES}
  ${TinyXML_LIBRARIES})

## Declare a cpp executable
add_executable(etherdaq_node src/etherdaq_node.cpp)
add_executable(bru_opt_publisher src/bru_opt_publisher.cpp)
add_executable(bru_opt_placebolt src/bru_opt_placebolt.cpp)

add_dependencies(bru_opt_publisher custom_msg_generate_messages_cpp)
add_dependencies(bru_opt_placebolt custom_msg_generate_messages_cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(etherdaq_node etherdaq_driver)
target_link_libraries(bru_opt_publisher ${catkin_LIBRARIES})
target_link_libraries(bru_opt_placebolt ${catkin_LIBRARIES})

#############
## Install ##
#############

## Mark executables and/or libraries for installation
 install(TARGETS etherdaq_driver etherdaq_node
   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )
