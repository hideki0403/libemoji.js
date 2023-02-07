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

du -sh ./externals/*

mkdir ./lib
cp ./tmp/**/*.{lib,a} ./lib

ls -lah ./
ls -lah ./externals/skia
ls -lah ./externals/skia/out/Static
ls -lah ./tmp
ls -lah ./lib

cd ../../
