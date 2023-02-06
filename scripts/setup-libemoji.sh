#!/bin/bash

cd ./externals/libemoji
sh ./externals/skia/tools/install_dependencies.sh
echo build libemoji

cmake .
make

cd ../../
