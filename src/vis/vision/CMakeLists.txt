cmake_minimum_required(VERSION 2.8.3)
project(vision)
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
  geometry_msgs
)


find_package(OpenCV)

add_message_files(
  FILES
  VectorData.msg
  imageCircleData.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
    CATKIN_DEPENDS message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

add_executable(bru_vis_grayImg src/bru_vis_grayImg.cpp)
add_executable(bru_vis_displayV2 src/bru_vis_displayV2.cpp)
add_executable(bru_vis_threshImg src/bru_vis_threshImg.cpp)
add_executable(bru_vis_circleDetection src/bru_vis_circleDetection.cpp)

add_dependencies(bru_vis_displayV2 vision_generate_messages_cpp)
add_dependencies(bru_vis_circleDetection vision_generate_messages_cpp)

target_link_libraries(bru_vis_grayImg ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
target_link_libraries(bru_vis_displayV2 ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
target_link_libraries(bru_vis_threshImg ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
target_link_libraries(bru_vis_circleDetection ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})

install(TARGETS bru_vis_grayImg
    RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(TARGETS bru_vis_displayV2
    RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(TARGETS bru_vis_threshImg
    RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(TARGETS bru_vis_circleDetection
    RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
