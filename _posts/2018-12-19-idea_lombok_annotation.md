---
layout: article
title: SpringBoot Lombok @Data 注解在Idea中生效
key: idea_SpringBoot_lombok_annotation 
tags:
  SpringBoot
---
Lombok 可以缩略POJO中大量getter、setter代码，配置一下，让Lombok在Idea中生效吧
<!--more-->
(从stackoverflow抄过来的)

## 依赖
```
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
```

## 配置
![](/assets/photo/20181219-enable-annotation-processors.png)

## 安插件
![](/assets/photo/2018121918-plugins-install.png)
安完插件之后还需要重启

## Thanks
[https://stackoverflow.com/questions/24006937/lombok-annotations-do-not-compile-under-intellij-idea](https://stackoverflow.com/questions/24006937/lombok-annotations-do-not-compile-under-intellij-idea)

