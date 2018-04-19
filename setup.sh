#!/bin/bash

MY_PATH="`dirname \"$0\"`"
cd $MY_PATH

virtualenv -p python3 .env
. .env/bin/activate

pip install --upgrade pip
pip install tensorflow matplotlib numpy scipy scikit-image pyte vtk sklearn

bash ./Rogue/build_with_no_monsters.sh
