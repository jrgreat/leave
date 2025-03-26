#14、传递一个用户名给脚本：
  #如果此用户的id号为0，则显示说这是管理员；
  #如果此用户的id号大于等于500，则显示说这是普通用户
  #否则，则说这是系统用户；
#!/bin/bash
id_num=`id $1 | awk -F "=" '{print $2}' | cut -d "(" -f1`
echo "id num is : $id_num"

if [[ $id_num -eq 0 ]]; then
echo "system administrator"
elif [[ $id_num -gt 500 ]]; then
echo "common user"
else
  echo "system user"
fi