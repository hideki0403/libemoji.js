@echo off
cd ./externals/libemoji

cd ./externals/depot_tools/
set PATH=%cd%;%PATH%
cd ../skia
python tools/git-sync-deps
tools\install_dependencies.sh

gn gen out/release -args='is_official_build=true is_component_build=false skia_use_system_expat = false skia_use_system_harfbuzz = false skia_use_system_icu = false skia_use_system_libjpeg_turbo = false skia_use_system_libpng = false skia_use_system_libwebp = false skia_use_system_zlib = false target_cpu="x64" cc="clang" cxx="clang++" clang_win="%LLVM_PATH%" win_vc="C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\VC"' extra_cflags=["-MTd"]
ninja -C out/release

cd ../../
