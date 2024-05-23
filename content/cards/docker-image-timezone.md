---
date created: 2023-12-27 00:33
date modified: 2024-05-22 20:02
title: Docker 镜像时区
slug: docker-image-timezone
feed: show
blog: tech
date: 2024-05-21
---
#Area/RD/运维/Docker

# docker 镜像时区

### 1. Alpine

根据[《Setting the timezone》](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fwiki.alpinelinux.org%2Fwiki%2FSetting_the_timezone)提示，我们可以将以下代码添加到 Dockerfile 中：

```dockerfile
ENV TZ Asia/Shanghai

RUN apk add tzdata && cp /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && apk del tzdata
```

### 2. Debian

Debian 基础镜像 中已经安装了 tzdata 包，我们可以将以下代码添加到 Dockerfile 中：

```dockerfile
ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*
```

### 3. Ubuntu

Ubuntu 基础镜像中没有安装了 tzdata 包，因此我们需要先安装 tzdata 包。

我们可以将以下代码添加到 Dockerfile 中。

```dockerfile
ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

RUN apt update \
    && apt install -y tzdata \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*
```

### 4. CentOS

CentOS 基础镜像 中已经安装了 tzdata 包，我们可以将以下代码添加到 Dockerfile 中。

```dockerfile
ENV TZ Asia/Shanghai

RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone
```

## thanks

- 雪梦科技 [Docker 时区调整方案-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1626811)
