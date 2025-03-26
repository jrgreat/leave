#12、通过命令行给定一个文件路径，而后判断：如果此文件中存在空白行，则显示其空白行的总数；否则，则显示无>空白行
#set -x
if [[ "$#" -lt 1 ]]; then
echo "need more parameters"
exit 1
fi

empty_space=`grep -E "^[[:space:]]*$" $1 | wc -l`
if [[ $empty_space -ne 0 ]]; then
    echo $empty_space
else
    echo "no empty space"
fi

