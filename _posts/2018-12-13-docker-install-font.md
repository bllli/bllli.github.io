---
layout: article
title: Docker 安装字体
key: docker-install-font
tags:
  docker
---

要在Docker中使用pdf生成工具，需要安装中文字体。仅在Dockerfile中COPY进去就行，不需要fc-cache

<!--more-->

Dockerfile:
```
COPY msyh.ttf /usr/share/fonts/msyh.ttf
```

# Thanks
[https://www.cnblogs.com/highend/p/docker_container_add_fonts.html](https://www.cnblogs.com/highend/p/docker_container_add_fonts.html)

