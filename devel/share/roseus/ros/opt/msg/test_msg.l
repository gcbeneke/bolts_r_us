;; Auto-generated. Do not edit!


(when (boundp 'opt::test_msg)
  (if (not (find-package "OPT"))
    (make-package "OPT"))
  (shadow 'test_msg (find-package "OPT")))
(unless (find-package "OPT::TEST_MSG")
  (make-package "OPT::TEST_MSG"))

(in-package "ROS")
;;//! \htmlinclude test_msg.msg.html


(defclass opt::test_msg
  :super ros::object
  :slots (_offSet ))

(defmethod opt::test_msg
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

(setf (get opt::test_msg :md5sum-) "e800213d1d061d690a2ce91f4c737f6b")
(setf (get opt::test_msg :datatype-) "opt/test_msg")
(setf (get opt::test_msg :definition-)
      "float64[6] offSet

")



(provide :opt/test_msg "e800213d1d061d690a2ce91f4c737f6b")


