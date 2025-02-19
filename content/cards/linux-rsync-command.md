---
title: → rsync
date created: 2024-04-02 16:37
date modified: 2024-08-16 11:50
slug: linux-rsync-command
tags:
  - Area/RD/运维/linux
---
 


自动对比差异，同步整个文件夹

```
--exclude 要用相对路径  
--partial 单文件断点续传
```


内网传输时可以不开启压缩 即不传 `-z` , 能提速很多 (20M/s -> 100M/s)

```bash
rsync -av -e ssh --exclude='*.out' /path/to/source/ user@hostB:/path/to/test/
```


## 指定端口号

```bash
rsync --progress --partial -av --rsh='ssh -p8080' -r /path/to/source user@host:/path/to/source
```
