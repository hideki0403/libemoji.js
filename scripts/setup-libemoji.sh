cd ./externals/libemoji
sh ./externals/skia/tools/install_dependencies.sh
echo build libemoji
cmake .

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  make
else
  msbuild emoji.sln
fi

cd ../../
