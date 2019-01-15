# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "abb_irb120_support: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iabb_irb120_support:/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(abb_irb120_support_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg" NAME_WE)
add_custom_target(_abb_irb120_support_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "abb_irb120_support" "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(abb_irb120_support
  "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/abb_irb120_support
)

### Generating Services

### Generating Module File
_generate_module_cpp(abb_irb120_support
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/abb_irb120_support
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(abb_irb120_support_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(abb_irb120_support_generate_messages abb_irb120_support_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg" NAME_WE)
add_dependencies(abb_irb120_support_generate_messages_cpp _abb_irb120_support_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(abb_irb120_support_gencpp)
add_dependencies(abb_irb120_support_gencpp abb_irb120_support_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS abb_irb120_support_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(abb_irb120_support
  "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/abb_irb120_support
)

### Generating Services

### Generating Module File
_generate_module_eus(abb_irb120_support
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/abb_irb120_support
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(abb_irb120_support_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(abb_irb120_support_generate_messages abb_irb120_support_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg" NAME_WE)
add_dependencies(abb_irb120_support_generate_messages_eus _abb_irb120_support_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(abb_irb120_support_geneus)
add_dependencies(abb_irb120_support_geneus abb_irb120_support_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS abb_irb120_support_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(abb_irb120_support
  "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/abb_irb120_support
)

### Generating Services

### Generating Module File
_generate_module_lisp(abb_irb120_support
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/abb_irb120_support
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(abb_irb120_support_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(abb_irb120_support_generate_messages abb_irb120_support_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg" NAME_WE)
add_dependencies(abb_irb120_support_generate_messages_lisp _abb_irb120_support_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(abb_irb120_support_genlisp)
add_dependencies(abb_irb120_support_genlisp abb_irb120_support_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS abb_irb120_support_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(abb_irb120_support
  "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/abb_irb120_support
)

### Generating Services

### Generating Module File
_generate_module_nodejs(abb_irb120_support
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/abb_irb120_support
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(abb_irb120_support_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(abb_irb120_support_generate_messages abb_irb120_support_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg" NAME_WE)
add_dependencies(abb_irb120_support_generate_messages_nodejs _abb_irb120_support_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(abb_irb120_support_gennodejs)
add_dependencies(abb_irb120_support_gennodejs abb_irb120_support_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS abb_irb120_support_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(abb_irb120_support
  "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/abb_irb120_support
)

### Generating Services

### Generating Module File
_generate_module_py(abb_irb120_support
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/abb_irb120_support
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(abb_irb120_support_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(abb_irb120_support_generate_messages abb_irb120_support_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/redouan/bolts_ws/src/irb/abb_irb120_support/msg/Forces.msg" NAME_WE)
add_dependencies(abb_irb120_support_generate_messages_py _abb_irb120_support_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(abb_irb120_support_genpy)
add_dependencies(abb_irb120_support_genpy abb_irb120_support_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS abb_irb120_support_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/abb_irb120_support)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/abb_irb120_support
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(abb_irb120_support_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/abb_irb120_support)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/abb_irb120_support
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(abb_irb120_support_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/abb_irb120_support)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/abb_irb120_support
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(abb_irb120_support_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/abb_irb120_support)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/abb_irb120_support
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(abb_irb120_support_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/abb_irb120_support)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/abb_irb120_support\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/abb_irb120_support
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(abb_irb120_support_generate_messages_py std_msgs_generate_messages_py)
endif()
