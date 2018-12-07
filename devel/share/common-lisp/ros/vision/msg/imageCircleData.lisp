; Auto-generated. Do not edit!


(cl:in-package vision-msg)


;//! \htmlinclude imageCircleData.msg.html

(cl:defclass <imageCircleData> (roslisp-msg-protocol:ros-message)
  ((vector_name
    :reader vector_name
    :initarg :vector_name
    :type cl:string
    :initform "")
   (allHolesDataVec
    :reader allHolesDataVec
    :initarg :allHolesDataVec
    :type (cl:vector vision-msg:VectorData)
   :initform (cl:make-array 0 :element-type 'vision-msg:VectorData :initial-element (cl:make-instance 'vision-msg:VectorData))))
)

(cl:defclass imageCircleData (<imageCircleData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <imageCircleData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'imageCircleData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision-msg:<imageCircleData> is deprecated: use vision-msg:imageCircleData instead.")))

(cl:ensure-generic-function 'vector_name-val :lambda-list '(m))
(cl:defmethod vector_name-val ((m <imageCircleData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-msg:vector_name-val is deprecated.  Use vision-msg:vector_name instead.")
  (vector_name m))

(cl:ensure-generic-function 'allHolesDataVec-val :lambda-list '(m))
(cl:defmethod allHolesDataVec-val ((m <imageCircleData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision-msg:allHolesDataVec-val is deprecated.  Use vision-msg:allHolesDataVec instead.")
  (allHolesDataVec m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <imageCircleData>) ostream)
  "Serializes a message object of type '<imageCircleData>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'vector_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'vector_name))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'allHolesDataVec))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'allHolesDataVec))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <imageCircleData>) istream)
  "Deserializes a message object of type '<imageCircleData>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'vector_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'vector_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'allHolesDataVec) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'allHolesDataVec)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'vision-msg:VectorData))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<imageCircleData>)))
  "Returns string type for a message object of type '<imageCircleData>"
  "vision/imageCircleData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'imageCircleData)))
  "Returns string type for a message object of type 'imageCircleData"
  "vision/imageCircleData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<imageCircleData>)))
  "Returns md5sum for a message object of type '<imageCircleData>"
  "f8a2a99d547045d060df3120b6af8431")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'imageCircleData)))
  "Returns md5sum for a message object of type 'imageCircleData"
  "f8a2a99d547045d060df3120b6af8431")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<imageCircleData>)))
  "Returns full string definition for message of type '<imageCircleData>"
  (cl:format cl:nil "# Message file which can be used to transfer a vector of circle data. For more info see VectorData.msg~%# Date: 04-12-2018~%# By: Giel Oomen~%~%string vector_name		# Name of the vector~%VectorData[] allHolesDataVec	# Vector of 'VectorData' structs (from VectorData.msg)~%~%~%================================================================================~%MSG: vision/VectorData~%# This message contains the structure of which the vector in imageCircleData.msg is made of. ~%# One place in the vector contains x, y, z and size values of one circle detected in the image.~%# Date: 04-12-2018	~%# By Giel Oomen~%~%float64 x	# Circle position on x-axis~%float64 y	# Circle position on y-axis~%float64 z	# Circle position on z-axis (depth in meters)~%float64 size	# Circle size ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'imageCircleData)))
  "Returns full string definition for message of type 'imageCircleData"
  (cl:format cl:nil "# Message file which can be used to transfer a vector of circle data. For more info see VectorData.msg~%# Date: 04-12-2018~%# By: Giel Oomen~%~%string vector_name		# Name of the vector~%VectorData[] allHolesDataVec	# Vector of 'VectorData' structs (from VectorData.msg)~%~%~%================================================================================~%MSG: vision/VectorData~%# This message contains the structure of which the vector in imageCircleData.msg is made of. ~%# One place in the vector contains x, y, z and size values of one circle detected in the image.~%# Date: 04-12-2018	~%# By Giel Oomen~%~%float64 x	# Circle position on x-axis~%float64 y	# Circle position on y-axis~%float64 z	# Circle position on z-axis (depth in meters)~%float64 size	# Circle size ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <imageCircleData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'vector_name))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'allHolesDataVec) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <imageCircleData>))
  "Converts a ROS message object to a list"
  (cl:list 'imageCircleData
    (cl:cons ':vector_name (vector_name msg))
    (cl:cons ':allHolesDataVec (allHolesDataVec msg))
))
