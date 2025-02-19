---
title: 使用 cloudflare workers 自建 docker 镜像代理
date created: 2024-08-08 10:16
date modified: 2024-11-21 16:52
slug: cloudflare-workers-docker-image-proxy
tags:
  - Area/RD/运维/Docker
  - Area/RD/折腾/CloudFlare
---
  

我按教程用 cloudflare workers  搭建了一个 docker 镜像代理。赞美大善人cloudflare，每天免费调用额度很难用完。

教程： https://www.cnblogs.com/guangdelw/p/18246236

我自己搭建的是 please.dengming.work

## 怎么使用？

### 1 
登陆dockerhub，为自己账号创建一个 "Public Repo Read-only" 等级的 personal-assess-token

https://app.docker.com/settings/personal-access-tokens

记录你的dockerhub用户名以及刚刚创建的 access token

### 2 
在你需要拉取镜像的服务器登录

```
docker login please.dengming.work -u <你的dockerhub用户名> 
// 再输入你的 access token
```

虽然这里登陆的是自己的域名，但实际会转接到 dockerhub 上

### 3

可以将域名加在前面镜像名字前面

```
docker pull redis:7
# 官方的 加/library
docker pull please.dengming.work/library/redis:7

docker pull n8nio/n8n
docker pull please.dengming.work/n8nio/n8n
```


也可以配置 docker 镜像源（需要重启 docker 服务）

```sh
vim /etc/docker/daemon.json
```

```json
{
  "registry-mirrors": [
   "https://docker.abc.com",
  ]
}
```