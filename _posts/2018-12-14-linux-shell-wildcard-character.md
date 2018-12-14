---
layout: article
title: Linux用通配符进行批量操作
key: linux-shell-wildcard-character 
tags:
  Linux
---
需要在服务器做批量删除操作，记录一下学习所得。
<!--more-->

批量创建
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

批量删除
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

