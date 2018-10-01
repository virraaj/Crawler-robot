#!/bin/bash
# Bash Menu Script Example

PS3='Please enter your choice: '
options=("Qlearning 1" "ValueIteration 2" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Qlearning 1")
            python Q-learning_V3.1.py
            ;;
        "ValueIteration 2")
            python valueiteratingpolicy.py
            ;;

        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
