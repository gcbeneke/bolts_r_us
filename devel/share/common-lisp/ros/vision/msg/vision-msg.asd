
(cl:in-package :asdf)

(defsystem "vision-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "VectorData" :depends-on ("_package_VectorData"))
    (:file "_package_VectorData" :depends-on ("_package"))
    (:file "imageCircleData" :depends-on ("_package_imageCircleData"))
    (:file "_package_imageCircleData" :depends-on ("_package"))
  ))