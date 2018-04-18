#!/bin/bash

MY_PATH="`dirname \"$0\"`"
cd $MY_PATH

pkill -9 -f python
pkill -9 -f rogue

if [ ! -d "log" ]; then
  mkdir log
fi
cd ./log
if [ ! -d "screenshots" ]; then
  mkdir screenshots
fi
if [ ! -d "performance" ]; then
  mkdir performance
fi
cd ..

. .env/bin/activate
python3 ./A3C/train.py