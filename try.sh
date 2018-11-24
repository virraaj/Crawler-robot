#!/bin/bash
# Bash Menu Script Example
pull_up_down=GPIO.PUD_DOWN
echo  "13" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio13/direction
echo "19" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio19/direction
echo "5" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio5/direction
echo "6" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio6/direction
cat /sys/class/gpio/gpio13/value
cat /sys/class/gpio/gpio19/value
cat /sys/class/gpio/gpio5/value
cat /sys/class/gpio/gpio6/value
val=$( cat /sys/class/gpio/gpio6/value)
val1=$(cat /sys/class/gpio/gpio5/value)
val2=$(cat /sys/class/gpio/gpio19/value)
val3=$(cat /sys/class/gpio/gpio13/value)
#echo val
#PS3='Please enter your choice: '
#options=("Qlearning 1" "ValueIteration 2" "Quit")
#select opt in "${options[@]}"
#do
#    case $opt in
#        "Qlearning 1")
#            python Q-learning_V3.1.py
#            ;;
#        "ValueIteration 2")
#            python valueiteratingpolicy.py
#            ;;
#
#        "Quit")
#            break
#            ;;
#        *) echo "invalid option $REPLY";;
#    esac
#done
a=1
echo "value of\"a\"is $a"
echo "val2 is $val2"

if [ $val2 == $a ]
then
  echo "Qlearning"
  python /home/pi/Crawler-robot/Q-learning_V3.1.py
elif [ $val3 == $a ]
then
  echo "Qlamdalearning"
  python /home/pi/Crawler-robot/qLamda_V1.2.py

else
  echo "value iteration"
  python /home/pi/Crawler-robot/valueiteratingpolicy.py
fi
if [ $val1 == $a ]
then
  echo "stop"
  #shutdown now
fi
