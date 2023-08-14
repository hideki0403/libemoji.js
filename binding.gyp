{
  "variables": {
    "conditions": [
      ['OS != "win"', {
        "libs": [
          "-L<(module_root_dir)/externals/libemoji/lib",
          "-Wl,-Bdynamic,-lpthread,-ldl,-lGL,-lGLU,-Bstatic,-lemoji,-lskia"
        ],
      }],
      ['OS == "win"', {
        "libs": [
          '<(module_root_dir)/externals/libemoji/lib/emoji',
          '<(module_root_dir)/externals/libemoji/lib/skia',
          '<(module_root_dir)/third_party/win/opengl32'
        ],
      }],
    ],
  },
  "targets": [
    {
      "target_name": "emoji",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "ldflags": [ "-static-libgcc" ],
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
