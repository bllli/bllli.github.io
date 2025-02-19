---
title: Docker 概念
date created: 2024-05-22 17:35
date modified: 2024-08-16 11:50
blog: tech
slug: docker-concepts
tags:
  - Area/RD/运维/Docker
---
 

- 镜像
- 容器
- 镜像仓库
	- 私有
		- harbor 自建
	- 公有
		- [Docker 拉取镜像 使用中国镜像站](cards/docker-pull-image-using-china-mirror)
		- 对于体积巨大的镜像，跨机房反正都是走公网。所以放docker hub 无所谓了，可以省硬盘空间


### Docker Desktop

安装在windows、mac、带桌面的linux发行版上, 用于本地开发环境
[orbstack macos上更好用的 docker desktop](cards/orbstack-a-better-alternative-to-docker-desktop-on-macos)

### Docker Engine

服务器上要安装 Docker Engine, 而不是 Docker Desktop  
[Install Docker Engine | Docker Documentation](https://docs.docker.com/engine/install/)