cmake_minimum_required(VERSION 2.8.3)
project(vis)
add_definitions(
    -std=c++11
)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  cv_bridge
  image_transport
  camera_info_manager
  sensor_msgs
  message_generation
)


find_package(OpenCV)

#add_message_files(
#FILES
#)

#generate_messages(
#  DEPENDENCIES
#  std_msgs
#)

catkin_package(
 #   CATKIN_DEPENDS message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

add_executable(bru_vis_color src/bru_vis_color.cpp)
target_link_libraries(bru_vis_color ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})

install(PROGRAMS

  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
