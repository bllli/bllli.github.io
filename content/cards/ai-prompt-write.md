---
title: 李继刚的模块化 prompt 的精确写法
date created: 2024-06-25 14:58
date modified: 2024-08-16 11:50
slug: ai-prompt-write
tags:
  - 兴趣/AIGC
---
 

目前写 Prompt 时, 经常根据不同需求添加不同模块要点, 固定的一个模式写法, 在面对差异巨大的需求场景时, 经常会因缺失某些描述而效果变差。

干脆下手整理一个从 A-Z ，共26 个角度的模块，使用时，可从其中挑选合适的模块组装。

- Attention: 需重点强调的要点
- Background: Prompt 的需求背景
- Constraints: 限制条件
- Definition: 名词定义
- Example: few-shots
- Fail: 处理失败时对应的兜底逻辑
- Goal: Prompt 要实现的目标
- Hack: 防止 Hack 的防护词
- In-depth: 一步步思考, 持续深入
- Job: 需求任务描述
- Knowledge: 知识库文件
- Lawful: 合法合规，安全行驶
- Merge: 是否使用多角色, 最终合并投票输出结果
- Neglect: 明确忽略哪些内容
- Odd: 偶尔[俏皮, 愤怒, 严肃]一下
- Pardon: 当用户回复信息不详细时, 持续追问
- Quote: 引用知识库信息时, 给出原文引用链接
- RAG:外挂知识库
- Skills: 擅长的技能项
- Tone: 回复使用的语气风格
- Unsure: 引入评判者视角, 当判定低于阈值时, 回复安全词
- Vaule: Prompt 模仿人格的价值观
- Workflow: 工作流程
- X-factor: 用户使用本 Prompt 最为重要的那个内核要素
- Yeow: Yeow, bro! Prompt 开场白设计
- Zig: 无厘头式 Prompt, 如[答案之书]

https://m.okjike.com/originalPosts/667a411cf2c1a920862a0393?s=ewoidSI6ICI1OTMzYmUxZjk1NTI5YjAwMTE5MzMxMWUiCn0= 