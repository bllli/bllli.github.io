---
title: pypi 国内源
date created: 2024-01-05 18:56
date modified: 2024-05-23 21:10
slug: pypi-chinese-source
---
#Area/RD/backend/python 

```
python -m pip install --upgrade pip
pip config set global.index-url https://mirrors.cernet.edu.cn/pypi/web/simple
```


- [[cards/nanjing-university-open-source-mirror|南京大学 开源镜像站]]
- [[cards/mirrorz-help-campus-joint-mirror|MirrorZ Help 校园联合镜像站]]


BUG !

使用 MirrorZ 有点问题

pip install -i https://mirrors.cernet.edu.cn/pypi/web/simple

https://mirrors.cernet.edu.cn/pypi/web/simple 302 到了 清华源
而清华源有一些包没有同步到最新
