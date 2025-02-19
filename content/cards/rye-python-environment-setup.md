---
title: rye  好用的 python 依赖管理工具
date created: 2024-07-23 11:47
date modified: 2024-12-28 23:27
slug: rye-python-environment-setup
tags:
  - Area/RD/python
---

官网 https://rye-up.com/  

- 直接安装在操作系统的软件，不依赖python，
- rye 管理 python 项目依赖，包括 python 及 python package
- rye 解析 package 的速度特别快
- 能够生成 requirement.lock 文件，能够固定pacakge版本，保证各环境依赖一致
- 能够生成 requirement.txt ，在打包时不需要安装 rye

缺点

- rye 会尝试去 python.org 下载 python 安装包，国内用户需要科学上网加速

### 对比 pdm 

https://pdm-project.org/en/latest/

pdm 依赖 python，我们需要手动在操作系统安装python，再安装 pdm

这意味着如果我同时有 3.10 / 3.12 两个python时，要安装两个pdm

更难受的是，如果你一个 3.10 的 venv 不小心执行了 3.12上安装的pdm命令时，会混乱


## 新项目用 uv 吧，别用 rye 了

2024-12-19 update

现在 rye 的大部分功能已经迁移到 同作者的 uv (https://github.com/astral-sh/uv) 中，新服务可以直接用 uv 了
