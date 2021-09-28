---
layout: article
title: Linux用通配符进行批量操作
key: linux-shell-wildcard-character 
tags:
  Linux
---
需要在服务器做批量删除操作，记录一下学习所得。
<!--more-->

## 批量创建
```
 $ mkdir demo-{1..3}{1..3}
 $ ll
total 0
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-11
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-12
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-13
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-21
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-22
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-23
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-31
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-32
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-33
```

## 批量删除
```shell
 $ rm -rf demo-{1..2}{1..2}
 $ ll
total 0
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-13
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-23
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-31
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-32
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-33

 $ rm -rf demo-{1,2}3
 $ ll
total 0
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-31
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-32
drwxr-xr-x  2 bllli  staff    64B Dec 14 17:47 demo-33

 $ rm -rf demo-3{1..3}
 $ ll
 $  # 删干净了
```

## ? 任意匹配1个字符

```shell
$ ll
[lidengming@alice logs]$ ll -h
total 150M
-rw-r--r-- 1 online online 437K Sep 28 20:40 alice-6001.log
-rw-r--r-- 1 online online 402K Sep 28 20:40 alice-6002.log

$ tail -f alice-600?.log

$ grep "DROP DATABASE;" alice-600?.log
```
