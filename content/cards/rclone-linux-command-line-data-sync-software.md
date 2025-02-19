---
title: Linux命令行数据同步软件 rclone
date created: 2024-11-18 17:02
date modified: 2024-11-22 16:39
tags:
  - Area/Life/NAS
slug: rclone-linux-command-line-data-sync-software
---



```
./rclone-v1.68.1-linux-amd64/rclone -P sync /vol2/1000/Photos/ remote:/rclone/nas-photos --exclude "*.~#0"

```


https://rclone.org/filtering/

同步扫描2万文件大概在60秒