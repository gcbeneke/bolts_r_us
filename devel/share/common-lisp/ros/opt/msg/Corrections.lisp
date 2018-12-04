; Auto-generated. Do not edit!


(cl:in-package opt-msg)


;//! \htmlinclude Corrections.msg.html

(cl:defclass <Corrections> (roslisp-msg-protocol:ros-message)
  ((offSet
    :reader offSet
    :initarg :offSet
    :type (cl:vector cl:float)
   :initform (cl:make-array 6 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass Corrections (<Corrections>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Corrections>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Corrections)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name opt-msg:<Corrections> is deprecated: use opt-msg:Corrections instead.")))

(cl:ensure-generic-function 'offSet-val :lambda-list '(m))
(cl:defmethod offSet-val ((m <Corrections>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader opt-msg:offSet-val is deprecated.  Use opt-msg:offSet instead.")
  (offSet m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Corrections>) ostream)
  "Serializes a message object of type '<Corrections>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'offSet))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Corrections>) istream)
  "Deserializes a message object of type '<Corrections>"
  (cl:setf (cl:slot-value msg 'offSet) (cl:make-array 6))
  (cl:let ((vals (cl:slot-value msg 'offSet)))
    (cl:dotimes (i 6)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Corrections>)))
  "Returns string type for a message object of type '<Corrections>"
  "opt/Corrections")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Corrections)))
  "Returns string type for a message object of type 'Corrections"
  "opt/Corrections")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Corrections>)))
  "Returns md5sum for a message object of type '<Corrections>"
  "e800213d1d061d690a2ce91f4c737f6b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Corrections)))
  "Returns md5sum for a message object of type 'Corrections"
  "e800213d1d061d690a2ce91f4c737f6b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Corrections>)))
  "Returns full string definition for message of type '<Corrections>"
  (cl:format cl:nil "float64[6] offSet~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Corrections)))
  "Returns full string definition for message of type 'Corrections"
  (cl:format cl:nil "float64[6] offSet~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Corrections>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'offSet) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Corrections>))
  "Converts a ROS message object to a list"
  (cl:list 'Corrections
    (cl:cons ':offSet (offSet msg))
))
