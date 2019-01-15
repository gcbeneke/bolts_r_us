
(cl:in-package :asdf)

(defsystem "abb_irb120_support-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Forces" :depends-on ("_package_Forces"))
    (:file "_package_Forces" :depends-on ("_package"))
  ))