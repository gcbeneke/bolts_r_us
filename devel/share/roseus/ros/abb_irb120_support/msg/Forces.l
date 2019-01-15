;; Auto-generated. Do not edit!


(when (boundp 'abb_irb120_support::Forces)
  (if (not (find-package "ABB_IRB120_SUPPORT"))
    (make-package "ABB_IRB120_SUPPORT"))
  (shadow 'Forces (find-package "ABB_IRB120_SUPPORT")))
(unless (find-package "ABB_IRB120_SUPPORT::FORCES")
  (make-package "ABB_IRB120_SUPPORT::FORCES"))

(in-package "ROS")
;;//! \htmlinclude Forces.msg.html


(defclass abb_irb120_support::Forces
  :super ros::object
  :slots (_p ))

(defmethod abb_irb120_support::Forces
  (:init
   (&key
    ((:p __p) (make-array 3 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _p __p)
   self)
  (:p
   (&optional __p)
   (if __p (setq _p __p)) _p)
  (:serialization-length
   ()
   (+
    ;; float64[3] _p
    (* 8    3)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[3] _p
     (dotimes (i 3)
       (sys::poke (elt _p i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[3] _p
   (dotimes (i (length _p))
     (setf (elt _p i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get abb_irb120_support::Forces :md5sum-) "1abbaca176899a0863a2922ff57df9ac")
(setf (get abb_irb120_support::Forces :datatype-) "abb_irb120_support/Forces")
(setf (get abb_irb120_support::Forces :definition-)
      "float64[3] p

")



(provide :abb_irb120_support/Forces "1abbaca176899a0863a2922ff57df9ac")


