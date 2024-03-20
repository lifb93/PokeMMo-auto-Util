#!/bin/sh

read -t 10 -p '你的系统是64位的么？[y/n]: ' choice
case $choice in
Y | y)
  echo '开始安装64位的pyHook 和 pyWin32'
  pip install ./src/pyHook/pyHook-1.5.1-cp37-cp37m-win_amd64.whl
  pip install ./src/pywin32/pywin32-306-cp37-cp37m-win_amd64.whl
  ;;
N | n)
  echo '开始安装32位的pyHook 和 pyWin32'
  pip install ./src/pyHook/pyHook-1.5.1-cp37-cp37m-win32.whl
  pip install ./src/pywin32/pywin32-306-cp37-cp37m-win32.whl
  ;;
esac
  echo '...'

sleep 3
