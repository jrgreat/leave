#17、添加10个用户：tuser501-tuser510；如果用户不存在，才添加；如果存在，则显示已经有此用户；显示一共添加了多少个用户。

#!/bin/bash

function check_usr_exist
{
    found=0
    usr=$1
    usrs=`cat /etc/passwd | awk -F ":" '{print $1}'`
    for id in $usrs; 
    do 
        if [[ $1 == $id ]];
        then
            found=1
        fi
    done
    echo $found    
}


let idx=0
for i in {1..10}; do
    new_usr="tuser50"$i
    exist=`check_usr_exist $new_usr`
    if [[ $exist -eq 0 ]]; then
        useradd $new_usr
        let idx=idx+1
    fi
done
echo "finally, newly create user number is: $idx"
