; Auto-generated. Do not edit!


(cl:in-package weiss_gripper_ieg76-srv)


;//! \htmlinclude SetForce-request.msg.html

(cl:defclass <SetForce-request> (roslisp-msg-protocol:ros-message)
  ((grasping_force
    :reader grasping_force
    :initarg :grasping_force
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SetForce-request (<SetForce-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetForce-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetForce-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name weiss_gripper_ieg76-srv:<SetForce-request> is deprecated: use weiss_gripper_ieg76-srv:SetForce-request instead.")))

(cl:ensure-generic-function 'grasping_force-val :lambda-list '(m))
(cl:defmethod grasping_force-val ((m <SetForce-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader weiss_gripper_ieg76-srv:grasping_force-val is deprecated.  Use weiss_gripper_ieg76-srv:grasping_force instead.")
  (grasping_force m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetForce-request>) ostream)
  "Serializes a message object of type '<SetForce-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'grasping_force)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetForce-request>) istream)
  "Deserializes a message object of type '<SetForce-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'grasping_force)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetForce-request>)))
  "Returns string type for a service object of type '<SetForce-request>"
  "weiss_gripper_ieg76/SetForceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetForce-request)))
  "Returns string type for a service object of type 'SetForce-request"
  "weiss_gripper_ieg76/SetForceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetForce-request>)))
  "Returns md5sum for a message object of type '<SetForce-request>"
  "b2ac4e15d384364f20affcca571143b9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetForce-request)))
  "Returns md5sum for a message object of type 'SetForce-request"
  "b2ac4e15d384364f20affcca571143b9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetForce-request>)))
  "Returns full string definition for message of type '<SetForce-request>"
  (cl:format cl:nil "uint8 grasping_force~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetForce-request)))
  "Returns full string definition for message of type 'SetForce-request"
  (cl:format cl:nil "uint8 grasping_force~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetForce-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetForce-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetForce-request
    (cl:cons ':grasping_force (grasping_force msg))
))
;//! \htmlinclude SetForce-response.msg.html

(cl:defclass <SetForce-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil)
   (message
    :reader message
    :initarg :message
    :type cl:string
    :initform ""))
)

(cl:defclass SetForce-response (<SetForce-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetForce-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetForce-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name weiss_gripper_ieg76-srv:<SetForce-response> is deprecated: use weiss_gripper_ieg76-srv:SetForce-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetForce-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader weiss_gripper_ieg76-srv:success-val is deprecated.  Use weiss_gripper_ieg76-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <SetForce-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader weiss_gripper_ieg76-srv:message-val is deprecated.  Use weiss_gripper_ieg76-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetForce-response>) ostream)
  "Serializes a message object of type '<SetForce-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetForce-response>) istream)
  "Deserializes a message object of type '<SetForce-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetForce-response>)))
  "Returns string type for a service object of type '<SetForce-response>"
  "weiss_gripper_ieg76/SetForceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetForce-response)))
  "Returns string type for a service object of type 'SetForce-response"
  "weiss_gripper_ieg76/SetForceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetForce-response>)))
  "Returns md5sum for a message object of type '<SetForce-response>"
  "b2ac4e15d384364f20affcca571143b9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetForce-response)))
  "Returns md5sum for a message object of type 'SetForce-response"
  "b2ac4e15d384364f20affcca571143b9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetForce-response>)))
  "Returns full string definition for message of type '<SetForce-response>"
  (cl:format cl:nil "bool success~%string message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetForce-response)))
  "Returns full string definition for message of type 'SetForce-response"
  (cl:format cl:nil "bool success~%string message~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetForce-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetForce-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetForce-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetForce)))
  'SetForce-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetForce)))
  'SetForce-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetForce)))
  "Returns string type for a service object of type '<SetForce>"
  "weiss_gripper_ieg76/SetForce")