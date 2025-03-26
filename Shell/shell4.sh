#4、新建10个用户tuser401-tuser410，并求他们的ID之和

#!/bin/bash

sum=0
for i in {0..10};
do 
  useradd user$i
  id_num=`id user$i | cut -d '=' -f2 | cut -d '(' -f1`
  let sum=sum+id_num
done
echo $sum 