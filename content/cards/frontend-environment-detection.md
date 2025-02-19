---
tags:
  - Area/RD/Frontend
title: 前端判断代码运行环境
date created: 2024-02-18 14:25
date modified: 2024-08-16 16:11
slug: frontend-environment-detection
---

我想在页面左上角增加当前的环境
如`[测试环境]后台管理系统`

前端如使用vite编译这种
js里用 `import.meta.env.VITE_KEY` 读取, 在 `.env` 文件里写了 `VITE_KEY=value`
那么在编译时, 这个 value 就确定了, 无法通过改变 `.env` 文件, 影响 `import.meta.env.VITE_KEY` 的值

可以通过读取当前url, 判断所运行的环境, 再根据环境决定使用

`[测试环境]后台管理系统`

`[生产环境]后台管理系统`