---
title: 解决 Quartz V4 标签重复
date created: 2024-08-16 11:32
date modified: 2024-08-16 11:49
slug: fix-quartz-v4-duplicate-tags
tags:
  - Area/PKM/quartz
---
 
## 问题

```
---
title: 李继刚的模块化 prompt 的精确写法
date created: 2024-06-25 14:58
date modified: 2024-06-26 18:38
slug: ai-prompt-write
---

#兴趣/AIGC 

目前写 Prompt 时, 经常根据不同需求添加不同
```

![Pasted image 20240816113720.png](/assets/pasted-image-20240816113720-21206b8372d18a0d574403c05bcbee50.png)

显示了两个 Tag，这很丑

## 发现

如果tags 在文件开头的 yaml中，就不会出现这个问题

https://raw.githubusercontent.com/davidwickerhf/maastrichtuniversity/v4/computerscience/BSc%20Computer%20Science/Concepts/Dense%20Graphs.md

```
---
tags: type/concept topic/x lang/x
type: concept
topic:
alias: 
---

## Relevant links
```


https://raw.githubusercontent.com/jackyzha0/quartz/v4/docs/features/folder%20and%20tag%20listings.md

```
---
title: Folder and Tag Listings
tags:
  - feature/emitter
---

Quartz emits listing pages for any folders and tags you have.

## Folder Listings
```

![Pasted image 20240816113600.png](/assets/pasted-image-20240816113600-7a3ed4ac823eef85d062441ccdd84b6f.png)

## 解决

Obsidian Linter 插件，将 tag 收集到文件开头的 yaml 里

![Pasted image 20240816114848.png](/assets/pasted-image-20240816114848-e7a48912c574835fd848a7ab583e4b23.png)