---
title: pip 安装一个包时,忽略某项依赖
date created: 2023-12-26 23:12
date modified: 2024-05-23 21:19
slug: pip-install-package-ignore-dependency
---

#Area/RD/backend/python 


volcengine 安装时依赖pycryptodome要gcc

用一种比较抽象的方法解决了

```
在 Docker python3.10-slim 中 volcengine 安装时报错, 其依赖 pycryptodome  显示 gcc 相关错误
调研发现 pycryptodome==3.19.0 不会报错, volcengine 依赖的 pycryptodome==3.9.9 会报错

修改方案是手动为 volcengine 安装依赖

1. 安装 pycryptodome==3.19.0
2. 拷贝出 volcengine 的 requirement.txt, 然后删掉  pycryptodome==3.9.9, 安装其余的依赖
3. 用 pip3 install --no-deps volcengine==1.0.111 忽略其依赖, 这样能够避免再安装  pycryptodome==3.9.9
```


Dockerfile 片段
```
COPY .devops/requirement-deps.txt /app  
RUN pip3 install pycryptodome==3.19.0 && pip3 install -r requirement-deps.txt && pip3 install --no-deps volcengine==1.0.111 && pip cache purge
```






