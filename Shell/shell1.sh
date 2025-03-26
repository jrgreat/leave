#1、写一个脚本
#  脚本可以接受一个以上的文件路径作为参数；
#显示每个文件所拥的行数；
#  显示本次共对多少个文件执行了行数统计。


FILE=$@
for FILE in "$@"
do
    LINE=`wc -l $FILE | awk '{print $1}'`
    echo "$FILE has [$LINE] lines"
done
echo "counted $# files"
