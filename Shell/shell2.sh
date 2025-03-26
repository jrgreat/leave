#2、分别计算100以内所有偶数之和和奇数之和

#!/bin/bash
let odd=0
let eve=0
for i in {0..100}; do
  #echo $i
  mod=$(($i%2))
  echo $mod
  if [[ $mod -eq 1 ]];
  then
  let "odd=odd+i"
  else
  let "eve=eve+i"
  fi
done
echo "odd=[$odd]"
echo "eve=[$eve]"

