;; Auto-generated. Do not edit!


(when (boundp 'opt::Corrections)
  (if (not (find-package "OPT"))
    (make-package "OPT"))
  (shadow 'Corrections (find-package "OPT")))
(unless (find-package "OPT::CORRECTIONS")
  (make-package "OPT::CORRECTIONS"))

(in-package "ROS")
;;//! \htmlinclude Corrections.msg.html


(defclass opt::Corrections
  :super ros::object
  :slots (_offSet ))

(defmethod opt::Corrections
  (:init
   (&key
    ((:offSet __offSet) (make-array 6 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _offSet __offSet)
   self)
  (:offSet
   (&optional __offSet)
   (if __offSet (setq _offSet __offSet)) _offSet)
  (:serialization-length
   ()
   (+
    ;; float64[6] _offSet
    (* 8    6)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[6] _offSet
     (dotimes (i 6)
       (sys::poke (elt _offSet i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[6] _offSet
   (dotimes (i (length _offSet))
     (setf (elt _offSet i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get opt::Corrections :md5sum-) "e800213d1d061d690a2ce91f4c737f6b")
(setf (get opt::Corrections :datatype-) "opt/Corrections")
(setf (get opt::Corrections :definition-)
      "float64[6] offSet

")



(provide :opt/Corrections "e800213d1d061d690a2ce91f4c737f6b")


