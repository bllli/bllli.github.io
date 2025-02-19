---
title: cursor, 一款基于 vscode 的 AI IDE
date created: 2024-08-13 14:58
date modified: 2024-12-30 14:07
slug: cursor-ai-ide-based-on-vscode
tags:
  - Area/RD/IDE
  - Work/share
  - 兴趣/AIGC/AI写代码
---

为大家推荐 cursor， 一款基于 vscode 的 AI IDE


## 下载地址

https://www.cursor.com/

文档 https://docs.cursor.com/

## 优点

- 能够为整个项目建立索引，生成代码更合逻辑
- 代码生成模式比 Github Copilot 好
	- 不局限于光标后的代码补全
	- 理解能力强
- IDE 基于 vscode 二次开发
	- vscode 插件兼容
	- 如果以前就用 vscode，很快就能熟悉
	- remote 开发功能能够正常使用

## 缺点

- 贵 20美元/月
- 依赖良好的网络环境



## 可以替换 LLM apikey ，but...

仅支持 chat 和 Ctrl+K 生成功能

杀手级应用 Cursor Tab (即AI联想补全功能) 还是要开通会员

---


## 规则文件

https://cursor.directory/

Copy and add a .cursorrules file in the root of your project.  
  
The instructions in the .cursorrules file will be included for features such as Cursor Chat and Ctrl/⌘ K.  
  
The more specific your rules for your project, the better.

此网站还有 cursor 使用教程 https://cursor.directory/learn

网站里面的规则 prompt 写的很好，给 AI 事无巨细地阐述技术栈、代码风格等

prompt 里有些部分程序员看了都会有收获
