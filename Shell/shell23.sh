#写一个猜数字脚本，当用户输入的数字和预设数字（随机生成一个小于100的数字）一样时，直接退出，否则让用户一直输入，并且提示用户的数字比预设数字大或者小。

#!/bin/bash

r=`echo $RANDOM`
n=$[$r%100]

while :
do 
    read -p "input number:" m
    if [[ $n -eq $m ]]; then
        echo "you are right! exit..."
        break
    elif [[ $n -gt $m ]]; 
    then 
        echo "please re-input a bigger one"
    else
        echo "please re-input a smaller one"
    fi
done