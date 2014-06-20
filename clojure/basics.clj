#!/usr/bin/env java -cp /path/to/clojure-1.2.0.jar clojure.main

(ns learnclojure)
(str "hello" " " "world")
(+ 1 2)
(= 1 1)
(= 1 2)
(not true)
(+ 1 (- 3 2)) ; a comment

(class 1) ; java.lang.Long
(class 1.) ; java.lang.Double
(class "") ; java.lang.String
(class false) ; java.lang.Boolean
(class nil) ; java.lang.??? -> null

'(+ 1 2) ; Don't evaluate
(quote (+ 1 2)) ; Same as above, don't evaluate

(class [1 2 3]) ; clojure.lang.PersistentVector
(class '(1 2 3)) ; clojure.lang.PersistentList
(list 1 2 3) ; same as '(1 2 3)

; collections
(coll? '(1 2 3)) ; PersistentList is a coll
(coll? [1 2 3]) ; PersitentVector is a coll

(seq? '(1 2 3)) ; a list IS a sequence
(seq? [1 2 3]) ; a vector is NOT a sequence


