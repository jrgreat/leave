#!/bin/bash
#7、显示当前系统上所有默认shell为bash的用户的用户名、UID及其所有此类用户的UID之和

info=`grep  '/bin/bash$' /etc/passwd | cut -d ":" -f1,3,7`
sum=0
for item in ${info};
do
    id=`echo $item | cut -d ":" -f2`
    let sum=sum+id
    echo "UID is $id"
    echo $item | cut -d ":" -f1
done
echo "SUM is $sum"
