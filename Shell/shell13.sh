#13、传递一个参数给脚本：
#  如果参数为quit，则显示说你要退出；
#  如果参数为yes，则显示说你要继续；
#  其它任意参数，则说无法识别。

#!/bin/bash

case $1 in
quit|Q)
    echo "quit"
    ;;
yes|Y)
    echo "continue"
    ;;
*)
    echo "don't know"
    ;;
esac
