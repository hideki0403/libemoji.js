#!/bin/bash

cd $WORKING_DIR/externals/libemoji
echo build libemoji

cmake . -DCMAKE_BUILD_TYPE=Release

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  make emoji_combined
else
  msbuild.exe emoji.sln -p:Configuration=Release
  mkdir ./lib
  cp ./tmp/*.lib ./lib || true
  cp ./tmp/**/*.lib ./lib || true
fi

ls -lah ./lib

cd ../../
