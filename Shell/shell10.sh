#10、通过命令行传递两个整数参数给脚本，脚本可以返回其大者

#!/bin/bash

if [[ $# -lt 2 ]]; then
  echo "need at least 2 parameters"
  exit 1
fi

echo "No.1 is $1"
echo "NO.2 is $2"
if [[ $1 -ge $2 ]]; then
    echo $1
else
    echo $2

fi
