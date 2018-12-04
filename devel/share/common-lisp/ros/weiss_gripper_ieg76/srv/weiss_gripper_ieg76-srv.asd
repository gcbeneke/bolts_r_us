
(cl:in-package :asdf)

(defsystem "weiss_gripper_ieg76-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Move" :depends-on ("_package_Move"))
    (:file "_package_Move" :depends-on ("_package"))
    (:file "SetForce" :depends-on ("_package_SetForce"))
    (:file "_package_SetForce" :depends-on ("_package"))
  ))