---
title: 火山引擎 对象存储 图片处理
date created: 2024-05-29 11:06
date modified: 2024-05-29 14:47
slug: volcengine-oss-image
---

#Area/RD/公有云 

https://www.volcengine.com/docs/6349/153626


把全部图片放在一个300x300的正方形内，保持图片笔记不变，同时正方形内空余部分补充白色

```
?x-tos-process=image/resize,w_300,h_300,m_pad,color_FFFFFF,limit_0
```
