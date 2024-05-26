---
title: Geohash
date created: 2024-02-26 12:05
date modified: 2024-05-26 11:12
slug: geohash
---

#Area/RD/backend 

通过用户坐标检索周围POI时，紧邻的POI可能在不同的geohash中，这样会导致明明在附近却检索不到

一般通过
1. 多检索周边一圈 （8个POI）
2. 检索时使用大一号的geohash

## 库

https://zhannicholas.github.io/posts/geography/understanding_geohash

有没有更好的?
