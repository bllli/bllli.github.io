---
title: docker-squash layer 压缩工具
slug: docker-squash-layer-compression-tool
date created: 2023-12-27 00:33
date modified: 2024-05-22 17:53
feed: show
blog: tech
date: 2024-05-21
---
#Area/RD/运维/Docker 

将image中的多个层(layer)压缩成1层
删除其中被覆盖的文件
从而减少镜像体积
image构建越不规范, 效果越好

[GitHub - goldmann/docker-squash: Docker image squashing tool](https://github.com/goldmann/docker-squash)

```
pip3 install docker-squash

$ docker-squash -h
usage: cli.py [-h] [-v] [--version] [-d] [-f FROM_LAYER] [-t TAG]
              [--tmp-dir TMP_DIR] [--output-path OUTPUT_PATH]
              image

Docker layer squashing tool

positional arguments:
  image                 Image to be squashed

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose output
  --version             Show version and exit
  -d, --development     Does not clean up after failure for easier debugging
  -f FROM_LAYER, --from-layer FROM_LAYER
                        Number of layers to squash or ID of the layer (or image ID or image name) to squash from.
                        In case the provided value is an integer, specified number of layers will be squashed.
                        Every layer in the image will be squashed if the parameter is not provided.
  -t TAG, --tag TAG     Specify the tag to be used for the new image. If not specified no tag will be applied
  -m MESSAGE, --message MESSAGE
                        Specify a commit message (comment) for the new image.
  -c, --cleanup         Remove source image from Docker after squashing
  --tmp-dir TMP_DIR     Temporary directory to be created and used
  --output-path OUTPUT_PATH
                        Path where the image may be stored after squashing.
  --load-image [LOAD_IMAGE]
                        Whether to load the image into Docker daemon after squashing
                        Default: true
```
