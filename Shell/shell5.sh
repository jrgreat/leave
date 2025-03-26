#5、写一个脚本
#  创建用户tuser501-tuser510; 
#创建目录/tmp/dir-当前日期时间；
#在/tmp/dir-当前日期时间，目录中创建10个空文件file101-file110
#将file101的属主改为tuser501，依次类推，一直将file110的属主改为tuser510。

FOLD_NAME=`date +%Y-%m-%d`
mkdir -p /tmp/dir-$FOLD_NAME
cd /tmp/dir-$FOLD_NAME
let BASE=500
let FILE=101
for i in {1..9}; 
do
    let num=BASE+$i
    useradd tuser$num
    let filenum=FILE+$i
    mkdir -p file$filenum
    chown tuser$num file$filenum
done

  