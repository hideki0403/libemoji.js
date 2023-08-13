{
  "variables": {
    "conditions": [
      ['OS != "win"', {
        "libs": [
          "-L<(module_root_dir)/externals/libemoji/lib",
          "-Wl,-Bstatic,-lemoji,-lskia"
        ],
      }],
      ['OS == "win"', {
        "libs": [
          '<(module_root_dir)/externals/libemoji/lib/emoji',
          '<(module_root_dir)/externals/libemoji/lib/skia'
        ],
      }],
    ],
  },
  "targets": [
    {
      "target_name": "emoji",
      "cflags!": [ "-fno-exceptions", "-no-pie" ],
      "cflags_cc!": [ "-fno-exceptions", "-no-pie" ],
      "ldflags": [
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
