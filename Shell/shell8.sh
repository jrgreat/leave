#!/bin/bash

#显示当前系统上有附加组的用户的用户名；并统计共有多少个此类用户

check_length_result=0
function check_length
{
    length=0
    list=$@
    for i in $list;
    do
        #echo $i
        let length=length+1
    done
    check_length_result=$length
}

users=`cat /etc/passwd | awk -F ":" '{print $1}'`
nums=0
for user in $users;
do
    each_group=`groups $user | awk -F ":" '{print $2}'`
    check_length_result=0
    check_length $each_group
    #echo "$user 's $check_length_result"
    if [[ $check_length_result -gt 1 ]]; then
        echo "$user has attached group"
        let nums=nums+1
    fi
done
echo "total attach group nums is [$nums]"