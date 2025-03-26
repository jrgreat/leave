#写脚本，用来实现交换两个文件或目录的名字。

if [[ $# -lt 2 ]]; then
echo "shall input more than 2 params"
exit 1
fi

if [ -f $1 ] && [ -f $2 ]; then 
    mv $1 tempfile
    mv $2 $1
    mv tempfile $2
fi
