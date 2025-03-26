#9、接受一个参数，这个参数是用户名；如果此用户存在，则显示其ID号
#!/bin/bash

users=`cat /etc/passwd | awk -F ":" '{print $1}'`

for user in $users; 
do
    if [[ "$user" == "$1" ]]; then
        uid=`id $user | cut -d '=' -f2 | cut -d '(' -f1`
        echo $uid
    fi
done
