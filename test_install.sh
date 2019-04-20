#!/bin/bash

# Test if the installation via setup.py works correctly

if [ "$#" -ne 1 ]; then
  echo "Usage: test_install.sh <v> (v = python version (2, 3))"
  exit 1
fi

VERSION=$1

if [ $VERSION == 2 ]; then
  VENV=virtualenv
else
  VENV=venv
fi

rm -rf venv
python$VERSION -m $VENV venv
source venv/bin/activate
python$VERSION setup.py install
# if we run `python -m diffimg` inside the current directory, it doesn't matter
# if we've installed it or not because it will use the local dir before the
# installed module
cd ..
python$VERSION -m \
  diffimg diffimg/images/mario-circle-cs.png \
  diffimg/images/mario-circle-node.png --delete

if [[ $? != 0 ]]; then
  echo -e "\nError installing"
  exit 1
else
  echo -e "\nInstall successful"
  exit 0
fi
