cd ./externals/libemoji
PATH="$(pwd)/externals/depot_tools:$PATH"
cd ./externals/skia

python tools/git-sync-deps
gn gen out/Static --args='is_debug=false target_cpu="x64" is_official_build=true'
ninja -C out/Static
cd ../../
