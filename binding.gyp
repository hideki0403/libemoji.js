{
  "variables": {
    "conditions": [
      ['OS != "win"', {
        "libs": [
          "-L<(module_root_dir)/externals/libemoji/lib",
          "-lemoji",
          "-ldl",
          "-lfontconfig",
          "-lfreetype",
          "-lpthread",
          "-lGL",
          "-lGLU"
        ],
      }],
      ['OS == "win"', {
        "libs": [
          '<(module_root_dir)/externals/libemoji/lib/emoji',
          '<(module_root_dir)/externals/libemoji/lib/skia',
          '<(module_root_dir)/thirdparty/fontconfig',
          '<(module_root_dir)/thirdparty/freetype',
          '<(module_root_dir)/thirdparty/pthread',
        ],
      }],
    ],
  },
  "targets": [
    {
      "target_name": "libemoji",
      "cflags!": [ "-fno-exceptions -MT" ],
      "cflags_cc!": [ "-fno-exceptions" ],
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
