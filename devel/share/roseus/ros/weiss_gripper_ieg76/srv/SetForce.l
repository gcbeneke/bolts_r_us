;; Auto-generated. Do not edit!


(when (boundp 'weiss_gripper_ieg76::SetForce)
  (if (not (find-package "WEISS_GRIPPER_IEG76"))
    (make-package "WEISS_GRIPPER_IEG76"))
  (shadow 'SetForce (find-package "WEISS_GRIPPER_IEG76")))
(unless (find-package "WEISS_GRIPPER_IEG76::SETFORCE")
  (make-package "WEISS_GRIPPER_IEG76::SETFORCE"))
(unless (find-package "WEISS_GRIPPER_IEG76::SETFORCEREQUEST")
  (make-package "WEISS_GRIPPER_IEG76::SETFORCEREQUEST"))
(unless (find-package "WEISS_GRIPPER_IEG76::SETFORCERESPONSE")
  (make-package "WEISS_GRIPPER_IEG76::SETFORCERESPONSE"))

(in-package "ROS")





(defclass weiss_gripper_ieg76::SetForceRequest
  :super ros::object
  :slots (_grasping_force ))

(defmethod weiss_gripper_ieg76::SetForceRequest
  (:init
   (&key
    ((:grasping_force __grasping_force) 0)
    )
   (send-super :init)
   (setq _grasping_force (round __grasping_force))
   self)
  (:grasping_force
   (&optional __grasping_force)
   (if __grasping_force (setq _grasping_force __grasping_force)) _grasping_force)
  (:serialization-length
   ()
   (+
    ;; uint8 _grasping_force
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _grasping_force
       (write-byte _grasping_force s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _grasping_force
     (setq _grasping_force (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass weiss_gripper_ieg76::SetForceResponse
  :super ros::object
  :slots (_success _message ))

(defmethod weiss_gripper_ieg76::SetForceResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _message (string __message))
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass weiss_gripper_ieg76::SetForce
  :super ros::object
  :slots ())

(setf (get weiss_gripper_ieg76::SetForce :md5sum-) "b2ac4e15d384364f20affcca571143b9")
(setf (get weiss_gripper_ieg76::SetForce :datatype-) "weiss_gripper_ieg76/SetForce")
(setf (get weiss_gripper_ieg76::SetForce :request) weiss_gripper_ieg76::SetForceRequest)
(setf (get weiss_gripper_ieg76::SetForce :response) weiss_gripper_ieg76::SetForceResponse)

(defmethod weiss_gripper_ieg76::SetForceRequest
  (:response () (instance weiss_gripper_ieg76::SetForceResponse :init)))

(setf (get weiss_gripper_ieg76::SetForceRequest :md5sum-) "b2ac4e15d384364f20affcca571143b9")
(setf (get weiss_gripper_ieg76::SetForceRequest :datatype-) "weiss_gripper_ieg76/SetForceRequest")
(setf (get weiss_gripper_ieg76::SetForceRequest :definition-)
      "uint8 grasping_force
---
bool success
string message

")

(setf (get weiss_gripper_ieg76::SetForceResponse :md5sum-) "b2ac4e15d384364f20affcca571143b9")
(setf (get weiss_gripper_ieg76::SetForceResponse :datatype-) "weiss_gripper_ieg76/SetForceResponse")
(setf (get weiss_gripper_ieg76::SetForceResponse :definition-)
      "uint8 grasping_force
---
bool success
string message

")



(provide :weiss_gripper_ieg76/SetForce "b2ac4e15d384364f20affcca571143b9")


