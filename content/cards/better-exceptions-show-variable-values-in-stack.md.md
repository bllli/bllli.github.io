---
title: better-exceptions 异常处理 在堆栈中展示涉及变量的值
date created: 2024-08-15 10:59
date modified: 2024-08-16 11:50
slug: better-exceptions-show-variable-values-in-stack.md
tags:
  - Area/RD/python
---
 

https://github.com/Qix-/better-exceptions

```
pip install better_exceptions
```

### 简单用法

#### 启用

```
export BETTER_EXCEPTIONS=1  # Linux / OSX
setx BETTER_EXCEPTIONS 1    # Windows
```

#### 不限制变量展示字符长度

```
import better_exceptions
better_exceptions.MAX_LENGTH = None
```
