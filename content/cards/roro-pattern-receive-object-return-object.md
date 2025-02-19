---
title: RORO Pattern, Receive Object & Return Object
date created: 2024-09-03 10:22
date modified: 2024-09-03 10:49
tags:
  - Area/RD/心法
slug: roro-pattern-receive-object-return-object
---

将函数的输入、输出都定义为一个对象，其用意是让读者清楚地知道函数的输入输出的数据格式。

Java 因语言特性多使用 [Java DTO, Data Transfer Object](cards/java-dto-data-transfer-object) ，天然倾向使用 RORO Pattern。

而在一些动态语言如 JavaScript 、 Python 中，函数的输入和输出可以是一个无具体定义的 hashmap (或称 dict) ，这会让其他人难以阅读、理解代码。当然此处的“其他人” 更有可能是一个月后的自己。

Python 建议使用 [pydantic，Python 中定义数据 schema 的首选](cards/pydantic-defining-data-schema-in-python) ，不建议使用 dataclass
