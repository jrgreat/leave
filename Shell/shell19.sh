#19、传递用户名给脚本
#判断此用户的shell是否为/bin/bash，如果是，则显示此用户为basher
#否则，则显示此用户为非basher


#!/bin/bash


bash_id=`cat /etc/passwd | grep $1 | awk -F ":" '{print $NF}'`
if [[ $bash_id == "/bin/bash" ]]; then 
echo "basher!\n"
else
echo "not basher\n"
fi
