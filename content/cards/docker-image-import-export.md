---
title: docker image 镜像导入导出
date created: 2024-08-14 10:59
date modified: 2024-11-21 17:54
tags:
  - Area/RD/运维/Docker
slug: docker-image-import-export
---
 
- 将 docker image 导出为一个文件
- 再将此文件移动到其他服务器上，将镜像导入docker

```
docker save dpage/pgadmin4 | gzip > pgadmin4.tar.gz
```


```
docker load < pgadmin4.tar.gz
```


作用：分发镜像、特殊网络环境导致只能传文件

缺点：多次传输时，每次导出都会带上全部 layer
