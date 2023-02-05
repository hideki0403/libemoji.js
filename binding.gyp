{
  "targets": [
    {
      "target_name": "libemoji",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "libraries": [
        "-L<(module_root_dir)/externals/libemoji/lib/",
        "-lemoji",
        "-ldl",
        "-lfontconfig",
        "-lfreetype",
        "-lGL",
        "-lGLU",
        "-lpthread"
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
