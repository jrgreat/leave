#打印乘法口诀

#!/bin/bash

for i in {1..9};do
  for j in {1..9}; do
    let result=i*j 
    echo "$i * $j = $result"
    done 
done