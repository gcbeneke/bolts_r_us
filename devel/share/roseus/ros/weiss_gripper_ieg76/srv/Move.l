;; Auto-generated. Do not edit!


(when (boundp 'weiss_gripper_ieg76::Move)
  (if (not (find-package "WEISS_GRIPPER_IEG76"))
    (make-package "WEISS_GRIPPER_IEG76"))
  (shadow 'Move (find-package "WEISS_GRIPPER_IEG76")))
(unless (find-package "WEISS_GRIPPER_IEG76::MOVE")
  (make-package "WEISS_GRIPPER_IEG76::MOVE"))
(unless (find-package "WEISS_GRIPPER_IEG76::MOVEREQUEST")
  (make-package "WEISS_GRIPPER_IEG76::MOVEREQUEST"))
(unless (find-package "WEISS_GRIPPER_IEG76::MOVERESPONSE")
  (make-package "WEISS_GRIPPER_IEG76::MOVERESPONSE"))

(in-package "ROS")





(defclass weiss_gripper_ieg76::MoveRequest
  :super ros::object
  :slots (_position ))

(defmethod weiss_gripper_ieg76::MoveRequest
  (:init
   (&key
    ((:position __position) 0.0)
    )
   (send-super :init)
   (setq _position (float __position))
   self)
  (:position
   (&optional __position)
   (if __position (setq _position __position)) _position)
  (:serialization-length
   ()
   (+
    ;; float32 _position
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _position
       (sys::poke _position (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _position
     (setq _position (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass weiss_gripper_ieg76::MoveResponse
  :super ros::object
  :slots (_success _message ))

(defmethod weiss_gripper_ieg76::MoveResponse
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

(defclass weiss_gripper_ieg76::Move
  :super ros::object
  :slots ())

(setf (get weiss_gripper_ieg76::Move :md5sum-) "68db0cb3ba325cf1de1b79dde3e8e0ea")
(setf (get weiss_gripper_ieg76::Move :datatype-) "weiss_gripper_ieg76/Move")
(setf (get weiss_gripper_ieg76::Move :request) weiss_gripper_ieg76::MoveRequest)
(setf (get weiss_gripper_ieg76::Move :response) weiss_gripper_ieg76::MoveResponse)

(defmethod weiss_gripper_ieg76::MoveRequest
  (:response () (instance weiss_gripper_ieg76::MoveResponse :init)))

(setf (get weiss_gripper_ieg76::MoveRequest :md5sum-) "68db0cb3ba325cf1de1b79dde3e8e0ea")
(setf (get weiss_gripper_ieg76::MoveRequest :datatype-) "weiss_gripper_ieg76/MoveRequest")
(setf (get weiss_gripper_ieg76::MoveRequest :definition-)
      "float32 position
---
bool success
string message

")

(setf (get weiss_gripper_ieg76::MoveResponse :md5sum-) "68db0cb3ba325cf1de1b79dde3e8e0ea")
(setf (get weiss_gripper_ieg76::MoveResponse :datatype-) "weiss_gripper_ieg76/MoveResponse")
(setf (get weiss_gripper_ieg76::MoveResponse :definition-)
      "float32 position
---
bool success
string message

")



(provide :weiss_gripper_ieg76/Move "68db0cb3ba325cf1de1b79dde3e8e0ea")


