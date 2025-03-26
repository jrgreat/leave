#18、添加10个用户：tuser601-tuser610；如果用户不存在，才添加，并以绿色显示添加成功；如果存在，则以红色显示已经有此用户；显示一共添加了多少个用户。

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

for i in {601..610}; do
    new_usr="tuser"$i
    exist=`check_usr_exist $new_usr`
    if [[ $exist -eq 0 ]]; then
        useradd $new_usr
        echo -e "\033[31mtuser$i\033[0m added successfully!\n"
    else
        echo -e "\033[32mtuser$i\033[0m exists!\n"
    fi
done

