#!/bin/bash

cd ./externals/libemoji
sh ./externals/skia/tools/install_dependencies.sh
echo build libemoji

cmake .

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  make
else
  msbuild.exe emoji.sln
fi

mkdir ./lib
cp ./tmp/*.{lib,a} ./lib

ls -lah ./tmp
ls -lah ./lib

cd ../../
