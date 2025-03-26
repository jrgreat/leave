#15、给定一个用户，如果其shell为/bin/bash且其ID号大于等于500，则说这是一个可登录普通用户；
#否则，则显示其为非登录用户或管理员。
#!/bin/bash

function get_id
{
    id_num=`id $1 | awk -F "=" '{print $2}' | cut -d "(" -f1`
    echo $id_num
}


function get_shell
{
    usr_shell=`cat /etc/passwd | grep $1 | awk -F ":" '{print $7}'`
    echo $usr_shell
}

usr_id=`get_id $1`
the_shell=`get_shell $1`
if [[ $usr_id -lt 500 ]];then
echo "not a login user or administrator"
elif [[ $the_shell == "/bin/bash" ]]; then
echo "a login user"
else
echo "none"
fi
