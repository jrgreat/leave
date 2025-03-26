#6、分别统计.bashrc、.profile和.bash_history文件中以#开头的行的行数和空白行数

for file in ~/.bashrc ~/.profile ~/.bash_history;
do
    echo "working on $file"
    line1=`grep -E '^#' $file |wc -l`
    echo "line number of start from # $line1"
    line2=`grep -E "^[[:space:]]*$" $file|wc -l`
    echo "line numeber of empty $line2"
done
    
    
