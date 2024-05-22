---
title: Docker 用进程pid查找该进程所属容器
slug: docker-find-container-by-process-pid
date created: 2023-12-27 00:33
date modified: 2024-05-22 19:28
feed: show
blog: tech
date: 2024-05-21
---
#Area/RD/运维/Docker  

在生产环境中排查系统异常，经常会遇到某个进程异常，如D状态。此时我们需要找出这个进程所属哪个容器，以便找到对应的应用服务器进行排查。

用进程pid查找该进程所属容器

直接从 `procfs` 找出进程的 `cgroup` 来确定所属容器:

```
cat /proc/<process-pid>/cgroup
```

此时会看到所属cgroup的字符串，这个字符串就对应容器id，可以进一步获取容器名字:

```
docker inspect <cgroup-id-prefix>
```


## thanks

https://cloud-atlas.readthedocs.io/zh-cn/latest/docker/debug/get_container_by_pid.html
