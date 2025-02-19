---
tags:
  - Area/RD/python/踩坑
title: python常见问题 xxx is not a package
date created: 2024-09-03 17:07
date modified: 2024-09-03 17:12
slug: python-common-issues-xxx-is-not-a-package
---
 

常见问题，import / from... import 代码报错，提示某包 "is not a package"

大概率是当前pythonpath中，存在一个.py文件与要导入的包重名

详细解释见

https://docs.python.org/3/reference/import.html
