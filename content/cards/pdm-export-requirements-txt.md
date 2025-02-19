---
title: pdm 导出 requirements.txt
date created: 2023-12-26 23:12
date modified: 2024-08-16 11:50
slug: pdm-export-requirements-txt
tags:
  - Area/RD/python
---
  

Dockerfile 里不想先安装pdm
(pdm本身也依赖python及一大堆第三方包)

```sh
pdm export --without-hashes > requirements.txt

pdm export -f requirements --without-hashes --prod > requirements.txt  

sed -i '' 's/;.*//' requirements.txt
```

pdm python包管理 弃用