#16、写一个脚本，如果某用户不存在，就添加

#!/bin/bash

users=`cat /etc/passwd | awk -F ":" '{print $1}'`
exist_user=0
for user in $users;
do 
    if [[ $user == "$1" ]]; then
        exist_user=1
    fi
done
if [[ $exist_user -eq 0 ]]; then
echo "user $1 doesn't exist, add it right now\n" 
useradd $1
else 
    echo "user $1 exist, nothing to do\n"
fi