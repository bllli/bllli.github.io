---
title: ssh port forwarding
date created: 2024-12-03 16:13
date modified: 2024-12-04 10:40
tags:
  - Area/RD/运维/linux
slug: ssh-port-forwarding
---

## 访问服务器的一个端口

1. 本机可以ssh到S1
2. 本机不能访问 S1:8888 端口

```
ssh -L 8888:localhost:8888 S1
```

## 将服务器作为代理，访问 ip:8888
1. 本机可以ssh到S1上
2. S1服务器可以访问到 ip:8888

```
ssh -L 8888:ip:8888 S1
```


## 完整

```
ssh -L <local port to point your browser toward>:<host name or IP of the web server>:<port that the web server is listening on> <valid user on server>@<server name or ip address>
```