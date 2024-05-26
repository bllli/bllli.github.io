---
title: → du 命令 查看文件夹大小
date created: 2023-12-27 00:33
date modified: 2024-05-24 10:46
slug: du-command-check-folder-size
---
#Area/RD/运维/linux

检查服务器硬盘剩余容量  
查看服务器硬盘已用大小

## mac

```
du -h -d 1
```

## linux

```
du -h --max-depth=1 .
```

[[cards/linux-df-command|→ df 命令 查看硬盘剩余空间]]