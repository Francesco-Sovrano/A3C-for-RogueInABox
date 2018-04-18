#!/bin/bash

MY_PATH="`dirname \"$0\"`"
cd $MY_PATH

apt-get install libncurses-dev

chmod -R 755 ./
cd ./rogue5.4.4-ant-r1.1.4
./configure
make clean
make
make install
