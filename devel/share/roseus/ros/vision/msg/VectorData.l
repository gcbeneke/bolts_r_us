;; Auto-generated. Do not edit!


(when (boundp 'vision::VectorData)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'VectorData (find-package "VISION")))
(unless (find-package "VISION::VECTORDATA")
  (make-package "VISION::VECTORDATA"))

(in-package "ROS")
;;//! \htmlinclude VectorData.msg.html


(defclass vision::VectorData
  :super ros::object
  :slots (_x _y _z _size ))

(defmethod vision::VectorData
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:size __size) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _size (float __size))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:size
   (&optional __size)
   (if __size (setq _size __size)) _size)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ;; float64 _size
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _size
       (sys::poke _size (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _size
     (setq _size (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get vision::VectorData :md5sum-) "6997b1ca28d937e14165cdb11acaa7bd")
(setf (get vision::VectorData :datatype-) "vision/VectorData")
(setf (get vision::VectorData :definition-)
      "# This message contains the structure of which the vector in imageCircleData.msg is made of. 
# One place in the vector contains x, y, z and size values of one circle detected in the image.
# Date: 04-12-2018	
# By Giel Oomen

float64 x	# Circle position on x-axis
float64 y	# Circle position on y-axis
float64 z	# Circle position on z-axis (depth in meters)
float64 size	# Circle size 

")



(provide :vision/VectorData "6997b1ca28d937e14165cdb11acaa7bd")


