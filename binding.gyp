{
  "variables": {
    "conditions": [
      ['OS != "win"', {
        "libs": [
          "-L<(module_root_dir)/externals/libemoji/lib",
          "-Wl,-Bdynamic,-lpthread,-ldl,-Bstatic,-lemoji,-lskia,-lfontconfig,-lfreetype,-lGL,-lGLU"
        ],
      }],
      ['OS == "win"', {
        "libs": [
          '<(module_root_dir)/externals/libemoji/lib/emoji',
          '<(module_root_dir)/externals/libemoji/lib/skia',
          '<(module_root_dir)/thirdparty/fontconfig',
          '<(module_root_dir)/thirdparty/freetype',
          '<(module_root_dir)/thirdparty/pthread',
          '<(module_root_dir)/thirdparty/opengl32'
        ],
      }],
    ],
  },
  "targets": [
    {
      "target_name": "emoji",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "ldflags": [
        "-static",
        "-static-libgcc",
        "-static-libstdc++"
      ],
      "libraries": [
        "<@(libs)"
      ],
      "sources": [ "src/main.cpp" ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "<(module_root_dir)/externals/libemoji/include"
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS', "NAPI_VERSION=<(napi_build_version)" ],
    }
  ]
}
