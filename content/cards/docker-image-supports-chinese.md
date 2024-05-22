---
title: Docker 镜像支持汉语
slug: docker-image-supports-chinese
date created: 2023-12-27 00:33
date modified: 2024-05-22 17:48
feed: show
blog: tech
date: 2024-05-21
---
#Area/RD/运维/docker 

```
apt update
apt install language-pack-zh-hans -y
locale -a
echo export LC_ALL='zh_CN.utf8' >> ~/.bashrc
source ~/.bashrc
echo 'hello' > 中文.log
ls
```

```
RUN apt update
RUN apt install language-pack-zh-hans -y
RUN locale -a
RUN echo export LC_ALL='zh_CN.utf8' >> ~/.bashrc
```
