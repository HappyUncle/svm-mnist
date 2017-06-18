#!/bin/bash

case $1 in
#train
train)
	svm/svm_multiclass_learn  -c 1.0 data/train.dat data/model.dat
;;

#test
test)
	svm/svm_multiclass_classify data/test.dat data/model.dat data/predict.dat
;;

*)
	echo 'please in train or test'
;;
esac
