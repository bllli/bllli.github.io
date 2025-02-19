---
title: Docker 中安装 LibreOffice
date created: 2024-07-04 10:32
date modified: 2024-11-21 17:55
tags:
  - Area/RD/运维/Docker
slug: install-libreoffice-docker
---
 

## 目的

在后端服务的 docker container 中，能够使用命令

```
/usr/bin/libreoffice --norestore --safe-mode --headless --convert-to txt 松果弹抖闪电鞭.doc --cat
```

此命令能够提取 doc / docx 中的文字为纯文本

## Dockerfile 

```
FROM python:3.12-slim
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends default-jre libreoffice-java-common libreoffice-common 
RUN apt-get install -y libreoffice-core
RUN apt-get install -y libreoffice-writer

# ADD tmp/松果弹抖闪电鞭.doc .
# # /usr/bin/libreoffice --norestore --safe-mode --headless --convert-to txt 松果弹抖闪电鞭.doc --cat
# CMD ["/usr/bin/libreoffice", "--norestore", "--safe-mode", "--headless", "--convert-to", "txt", "松果弹抖闪电鞭.doc", "--cat"]
```

## image size

增加了1.3G

```

REPOSITORY                                                       TAG                  IMAGE ID       CREATED          SIZE
python-libreoffice   3.12-slim-squashed   7248c4a20bc6   10 minutes ago   1.46GB
python-libreoffice   3.12-slim            a8750e727c5c   15 minutes ago   1.47GB
python                                                           3.12-slim            36d84f5948d0   7 days ago       129MB
```

无需使用 [docker-squash layer 压缩工具](cards/docker-squash-layer-compression-tool) ，我试过，只压缩掉几M

## LibreOffice Error: source file could not be loaded

少装了LibreOffice的writer

```sh
yum install libreoffice-writer
```

