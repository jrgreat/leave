#11、通过命令行传递任意个整数参数给脚本，脚本可以返回其大者

#!/bin/bash

if [[ $# -lt 1 ]]; then
  echo "need at least 2 parameters"
  exit 1
fi

nums=$@
biggest=$1
for num in $nums;
do
    if [[ $biggest -lt $num  ]]; then 
        biggest=$num
    fi
done
echo $biggest

