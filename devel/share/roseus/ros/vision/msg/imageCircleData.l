;; Auto-generated. Do not edit!


(when (boundp 'vision::imageCircleData)
  (if (not (find-package "VISION"))
    (make-package "VISION"))
  (shadow 'imageCircleData (find-package "VISION")))
(unless (find-package "VISION::IMAGECIRCLEDATA")
  (make-package "VISION::IMAGECIRCLEDATA"))

(in-package "ROS")
;;//! \htmlinclude imageCircleData.msg.html


(defclass vision::imageCircleData
  :super ros::object
  :slots (_vector_name _allHolesDataVec ))

(defmethod vision::imageCircleData
  (:init
   (&key
    ((:vector_name __vector_name) "")
    ((:allHolesDataVec __allHolesDataVec) (let (r) (dotimes (i 0) (push (instance vision::VectorData :init) r)) r))
    )
   (send-super :init)
   (setq _vector_name (string __vector_name))
   (setq _allHolesDataVec __allHolesDataVec)
   self)
  (:vector_name
   (&optional __vector_name)
   (if __vector_name (setq _vector_name __vector_name)) _vector_name)
  (:allHolesDataVec
   (&rest __allHolesDataVec)
   (if (keywordp (car __allHolesDataVec))
       (send* _allHolesDataVec __allHolesDataVec)
     (progn
       (if __allHolesDataVec (setq _allHolesDataVec (car __allHolesDataVec)))
       _allHolesDataVec)))
  (:serialization-length
   ()
   (+
    ;; string _vector_name
    4 (length _vector_name)
    ;; vision/VectorData[] _allHolesDataVec
    (apply #'+ (send-all _allHolesDataVec :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _vector_name
       (write-long (length _vector_name) s) (princ _vector_name s)
     ;; vision/VectorData[] _allHolesDataVec
     (write-long (length _allHolesDataVec) s)
     (dolist (elem _allHolesDataVec)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _vector_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _vector_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; vision/VectorData[] _allHolesDataVec
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _allHolesDataVec (let (r) (dotimes (i n) (push (instance vision::VectorData :init) r)) r))
     (dolist (elem- _allHolesDataVec)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get vision::imageCircleData :md5sum-) "f8a2a99d547045d060df3120b6af8431")
(setf (get vision::imageCircleData :datatype-) "vision/imageCircleData")
(setf (get vision::imageCircleData :definition-)
      "# Message file which can be used to transfer a vector of circle data. For more info see VectorData.msg
# Date: 04-12-2018
# By: Giel Oomen

string vector_name		# Name of the vector
VectorData[] allHolesDataVec	# Vector of 'VectorData' structs (from VectorData.msg)


================================================================================
MSG: vision/VectorData
# This message contains the structure of which the vector in imageCircleData.msg is made of. 
# One place in the vector contains x, y, z and size values of one circle detected in the image.
# Date: 04-12-2018	
# By Giel Oomen

float64 x	# Circle position on x-axis
float64 y	# Circle position on y-axis
float64 z	# Circle position on z-axis (depth in meters)
float64 size	# Circle size 

")



(provide :vision/imageCircleData "f8a2a99d547045d060df3120b6af8431")


