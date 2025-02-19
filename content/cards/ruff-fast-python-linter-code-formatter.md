---
title: Python code formatter Ruff
date created: 2023-12-27 13:59
date modified: 2024-12-03 19:44
slug: ruff-fast-python-linter-code-formatter
tags:
  - Area/RD/python
---

团队内使用统一的代码格式化工具可以提高代码可读性、可维护性与协作效率。

向大家介绍 Ruff，它是一款轻量、高效的 python 代码格式化工具

官网： https://docs.astral.sh/ruff/

## 优点

与传统 python 代码格式化工具（ black autopep8）相比

1. ruff 速度特别快(10-100倍)，非常适合保存文件时自动触发代码格式化
2. 不需要折腾插件，默认配置已经足够好

## 与 vscode 集成

安装插件： https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff
（或直接搜索 ruff）

项目根目录/.vscode/settings.json
(可以忽略 `files.exclude` / `cSpell.words` ) 
```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": "always",
    "source.organizeImports": "always"
  },
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "always",
      "source.organizeImports": "always"
    },
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "files.exclude": {
    "**/.git": true,
    "**/.svn": true,
    "**/.hg": true,
    "**/CVS": true,
    "**/.DS_Store": true,
    "**/Thumbs.db": true,
    ".pytest_cache": true,
    ".venv": true,
    "**/__pycache__": true
  },
  "python.analysis.typeCheckingMode": "basic",
  "cSpell.words": ["Langfuse"]
}

```

## 我最开始了解 ruff ：FastAPI 用 ruff 替代了 autoflake

https://github.com/tiangolo/fastapi/commit/fa74093440aaff710009ed23646eb804417b26fc