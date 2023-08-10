#!/bin/bash

cd $WORKING_DIR/externals/libemoji
sh ./externals/skia/tools/install_dependencies.sh
echo build skia

cmake . -DCMAKE_BUILD_TYPE=Release

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  make skia
else
  msbuild.exe emoji.sln -target:skia -p:Configuration=Release
fi
