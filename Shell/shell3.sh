#!/bin/bash

#3、计算当前系统上所有用户的ID之和

let sum=0
for user in `getent passwd | awk -F ":" '{print $1}'`; 
do echo $user;
id_sum=`id $user | cut -d '=' -f2 | cut -d '(' -f1`
let sum=sum+id_sum
done
echo $sum