#!/bin/bash

DIRECTORY=$WORKING_DIR/externals/libemoji
cd $DIRECTORY

if [[ "$CREATE_SYMBOLIC_LINK" == "true" ]]; then
  # Move external repos to C drive
  echo "export MSYS=winsymlinks:nativestrict" > ~/.bashrc
  source ~/.bashrc

  echo "Create symbolic link"
  mkdir -p "C:/buildtmp"
  mv "$DIRECTORY/externals" "C:/buildtmp"
  ln -s "C:/buildtmp/externals" "$DIRECTORY/externals"
  echo "successfully create symbolic link!" > "$DIRECTORY/externals/test.txt"
  cat "C:/buildtmp/externals/test.txt"
fi

gn_path=$DIRECTORY/externals/depot_tools/gn.py
ninja_path=$DIRECTORY/externals/depot_tools/ninja.py

sh ./externals/skia/tools/install_dependencies.sh
echo build skia

cmake . -DCMAKE_BUILD_TYPE=Release

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  make skia
else
  msbuild.exe emoji.sln -target:skia -p:Configuration=Release
fi
