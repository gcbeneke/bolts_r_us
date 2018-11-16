
(cl:in-package :asdf)

(defsystem "opt-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Corrections" :depends-on ("_package_Corrections"))
    (:file "_package_Corrections" :depends-on ("_package"))
    (:file "OptoForceData" :depends-on ("_package_OptoForceData"))
    (:file "_package_OptoForceData" :depends-on ("_package"))
  ))