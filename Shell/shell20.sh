#20、给定一个文件路径
#判断此文件是否存在；不存在，则说明文件不存，并直接结束脚本；
#如果文件是普通文件，则显示为“regular file”；
#如果文件是目录，则显示为“directory”；
#如果文件是链接文件，则显示为“Symbolic file";
#否则，则显示为“unknown type.”


if [ ! -e $1 ]; then
echo "file does not exist"
exit 1
fi
if [ -L $1 ];then
  echo "Symbolic file."
elif [ -d $1 ];then
  echo "directory."
elif [ -f $1 ];then
  echo "regular file."
else
  echo "unknown type."
fi

