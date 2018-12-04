# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "weiss_gripper_ieg76: 0 messages, 2 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(weiss_gripper_ieg76_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv" NAME_WE)
add_custom_target(_weiss_gripper_ieg76_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "weiss_gripper_ieg76" "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv" ""
)

get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv" NAME_WE)
add_custom_target(_weiss_gripper_ieg76_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "weiss_gripper_ieg76" "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(weiss_gripper_ieg76
  "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/weiss_gripper_ieg76
)
_generate_srv_cpp(weiss_gripper_ieg76
  "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/weiss_gripper_ieg76
)

### Generating Module File
_generate_module_cpp(weiss_gripper_ieg76
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/weiss_gripper_ieg76
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(weiss_gripper_ieg76_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(weiss_gripper_ieg76_generate_messages weiss_gripper_ieg76_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv" NAME_WE)
add_dependencies(weiss_gripper_ieg76_generate_messages_cpp _weiss_gripper_ieg76_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv" NAME_WE)
add_dependencies(weiss_gripper_ieg76_generate_messages_cpp _weiss_gripper_ieg76_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(weiss_gripper_ieg76_gencpp)
add_dependencies(weiss_gripper_ieg76_gencpp weiss_gripper_ieg76_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS weiss_gripper_ieg76_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(weiss_gripper_ieg76
  "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/weiss_gripper_ieg76
)
_generate_srv_eus(weiss_gripper_ieg76
  "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/weiss_gripper_ieg76
)

### Generating Module File
_generate_module_eus(weiss_gripper_ieg76
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/weiss_gripper_ieg76
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(weiss_gripper_ieg76_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(weiss_gripper_ieg76_generate_messages weiss_gripper_ieg76_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv" NAME_WE)
add_dependencies(weiss_gripper_ieg76_generate_messages_eus _weiss_gripper_ieg76_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv" NAME_WE)
add_dependencies(weiss_gripper_ieg76_generate_messages_eus _weiss_gripper_ieg76_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(weiss_gripper_ieg76_geneus)
add_dependencies(weiss_gripper_ieg76_geneus weiss_gripper_ieg76_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS weiss_gripper_ieg76_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(weiss_gripper_ieg76
  "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/weiss_gripper_ieg76
)
_generate_srv_lisp(weiss_gripper_ieg76
  "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/weiss_gripper_ieg76
)

### Generating Module File
_generate_module_lisp(weiss_gripper_ieg76
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/weiss_gripper_ieg76
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(weiss_gripper_ieg76_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(weiss_gripper_ieg76_generate_messages weiss_gripper_ieg76_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv" NAME_WE)
add_dependencies(weiss_gripper_ieg76_generate_messages_lisp _weiss_gripper_ieg76_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv" NAME_WE)
add_dependencies(weiss_gripper_ieg76_generate_messages_lisp _weiss_gripper_ieg76_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(weiss_gripper_ieg76_genlisp)
add_dependencies(weiss_gripper_ieg76_genlisp weiss_gripper_ieg76_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS weiss_gripper_ieg76_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(weiss_gripper_ieg76
  "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/weiss_gripper_ieg76
)
_generate_srv_nodejs(weiss_gripper_ieg76
  "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/weiss_gripper_ieg76
)

### Generating Module File
_generate_module_nodejs(weiss_gripper_ieg76
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/weiss_gripper_ieg76
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(weiss_gripper_ieg76_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(weiss_gripper_ieg76_generate_messages weiss_gripper_ieg76_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv" NAME_WE)
add_dependencies(weiss_gripper_ieg76_generate_messages_nodejs _weiss_gripper_ieg76_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv" NAME_WE)
add_dependencies(weiss_gripper_ieg76_generate_messages_nodejs _weiss_gripper_ieg76_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(weiss_gripper_ieg76_gennodejs)
add_dependencies(weiss_gripper_ieg76_gennodejs weiss_gripper_ieg76_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS weiss_gripper_ieg76_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(weiss_gripper_ieg76
  "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/weiss_gripper_ieg76
)
_generate_srv_py(weiss_gripper_ieg76
  "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/weiss_gripper_ieg76
)

### Generating Module File
_generate_module_py(weiss_gripper_ieg76
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/weiss_gripper_ieg76
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(weiss_gripper_ieg76_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(weiss_gripper_ieg76_generate_messages weiss_gripper_ieg76_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/SetForce.srv" NAME_WE)
add_dependencies(weiss_gripper_ieg76_generate_messages_py _weiss_gripper_ieg76_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/gijs/bolts_ws/src/weiss_gripper_ieg76/srv/Move.srv" NAME_WE)
add_dependencies(weiss_gripper_ieg76_generate_messages_py _weiss_gripper_ieg76_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(weiss_gripper_ieg76_genpy)
add_dependencies(weiss_gripper_ieg76_genpy weiss_gripper_ieg76_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS weiss_gripper_ieg76_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/weiss_gripper_ieg76)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/weiss_gripper_ieg76
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(weiss_gripper_ieg76_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/weiss_gripper_ieg76)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/weiss_gripper_ieg76
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(weiss_gripper_ieg76_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/weiss_gripper_ieg76)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/weiss_gripper_ieg76
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(weiss_gripper_ieg76_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/weiss_gripper_ieg76)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/weiss_gripper_ieg76
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(weiss_gripper_ieg76_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/weiss_gripper_ieg76)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/weiss_gripper_ieg76\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/weiss_gripper_ieg76
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(weiss_gripper_ieg76_generate_messages_py std_msgs_generate_messages_py)
endif()
