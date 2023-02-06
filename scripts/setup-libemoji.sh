#!/bin/bash

cd ./externals/libemoji
sh ./externals/skia/tools/install_dependencies.sh
echo build libemoji

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  cmake .
  make
else
  cmake . -G "MinGW Makefiles"
  make
fi

cd ../../
