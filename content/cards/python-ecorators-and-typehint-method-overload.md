---
title: python 装饰器和typehit重载
date created: 2024-10-14 16:58
date modified: 2024-12-27 19:02
slug: python-ecorators-and-typehint-method-overload
tags:
  - Area/RD/python/feature
---
 
1. 实际上还是一个函数
2. 提供两种不同的用法，以便指示python typehit 按你的预期工作


```python
from typing import Any, Callable, Optional, TypeVar, overload

F = TypeVar("F", bound=Callable[..., Any])


# python 的装饰器实际上是一个以函数为参数的函数


class LogDecorator:
    @overload
    def log_it(self, func: F) -> F: ...

    @overload
    def log_it(
        self, func: None = None, *, name: Optional[str] = None
    ) -> Callable[[F], F]: ...

    def log_it(
        self, func: Optional[F] = None, *, name: Optional[str] = None
    ) -> Callable[[F], F]:
        def decorator(func: F) -> F:
            print(name, func)
            return func

        if func is None:
            return decorator
        return decorator(func)


log_decorator = LogDecorator()
log_it = log_decorator.log_it


@log_it
def f():
    print("f")


f()


@log_it(name="g")
def g():
    print("g")


g()

```


---

学习自 [langfuse Prompt Management](cards/langfuse-prompt-management)  的 python SDK