---
title: The 70% problem. Hard truths about AI-assisted coding
date created: 2024-12-06 17:41
date modified: 2024-12-10 10:28
tags:
  - 兴趣/AIGC/AI写代码
slug: 70-percent-problem-hard-truths-about-ai-assisted-coding
---

- 原文： https://addyo.substack.com/p/the-70-problem-hard-truths-about
- 讨论： https://news.ycombinator.com/item?id=42336553

--- 
讨论摘抄

Every generation has to learn “There is no silver bullet”.

There are essential tasks and there are accidental tasks. The tools really only help with the accidental tasks.

本质任务和偶然任务，工具真正能帮助的只是偶然任务。

--- 

原文摘抄

## AI 辅助编程的两种模式

#### 0 到 MVP

- 从设计稿或粗略概念开始
- 使用AI生成完整代码库
- 几小时/几天就得到一个原型
- 快速验证、迭代

极短时间内将一个设计稿转化为一个可运行的网页应用，虽然并没有达到生产环境就绪状态，但也能获取初步的用户反馈

####  日常开发

- 代码补全
- 代码重构
- 生成测试和文档
- 与AI结对编程解决问题


这两种方法都能够显著加速开发进程，但他们有背后的隐藏成本

### The hidden cost of "AI Speed"
当一个资深工程师在使用AI辅助工具时，有个关键的细节：他们并非一味接受AI的建议。他们始终在：

- 将生成出的代码重构为更小、更加专注的模块
- 添加AI遗漏的边缘情况处理
- 强化类型定义和接口
- 质疑架构决策
- 增加全面的错误处理

换句话说，他们正在运用多年积累的工程智慧来塑造和约束 AI 的输出。AI 加速了他们的实现过程，但他们的专业知识才是保持代码可维护性的关键。

**I've watched senior engineers use AI to:  
我曾目睹资深工程师运用 AI：**

- Rapidly prototype ideas they already understand  
    快速原型化他们已理解的想法
    
- Generate basic implementations they can then refine  
    生成基础实现以便进一步精炼
    
- Explore alternative approaches to known problems  
    探索已知问题的替代解决方案
    
- Automate routine coding tasks  
    自动化常规编码任务

The most successful non-engineers I've seen using AI coding tools take a hybrid approach:  
我见过的最成功的非工程师使用 AI 编码工具时，采取的是一种混合方法：

1. Use AI for rapid prototyping  
    利用 AI 进行快速原型设计
    
2. Take time to understand how the generated code works  
    花时间理解生成的代码如何运作
    
3. Learn basic programming concepts alongside AI usage  
    学习基本编程概念与人工智能应用并行
    
4. Build up a foundation of knowledge gradually  
    逐步构建知识基础
    
5. Use AI as a learning tool, not just a code generator  
    将 AI 作为学习工具，而不仅仅是代码生成器
    

But this requires patience and dedication - exactly the opposite of what many people hope to achieve by using AI tools in the first place.  
但这需要耐心和专注——恰恰与许多人最初希望通过使用 AI 工具所追求的相反。


## What actually works: practical patterns  
实际有效的做法：实用模式

After observing dozens of teams, here's what I've seen work consistently:  
在观察了数十个团队后，我发现以下模式始终有效：

### 1. The "AI first draft" pattern  
1. “AI 初稿”模式

- Let AI generate a basic implementation  
    让 AI 生成一个基础实现
    
- Manually review and refactor for modularity  
    手动审查并重构以提高模块化
    
- Add comprehensive error handling  
    添加全面的错误处理
    
- Write thorough tests 编写详尽测试
    
- Document key decisions 记录关键决策
    

### 2. The "Constant conversation" pattern  
2. “持续对话”模式

- Start new AI chats for each distinct task  
    为每个独立任务开启新的 AI 聊天
    
- Keep context focused and minimal  
    保持上下文集中且精简
    
- Review and commit changes frequently  
    频繁审查并提交更改
    
- Maintain tight feedback loops  
    保持紧密的反馈循环
    

### 3. The "Trust but verify" pattern  
3. “信任但要验证”模式

- Use AI for initial code generation  
    使用 AI 进行初始代码生成
    
- Manual review of all critical paths  
    手动审查所有关键路径
    
- Automated testing of edge cases  
    自动化测试边缘情况
    
- Regular security audits 定期进行安全审计

## What does this mean for you?  
这对您意味着什么？

If you're just starting with AI-assisted development, here's my advice:  
如果你刚开始接触 AI 辅助开发，我的建议是：

1. **Start small 从小处着手**
    
    - Use AI for isolated, well-defined tasks  
        利用 AI 处理独立且定义明确的任务
        
    - Review every line of generated code  
        逐行审查生成的代码
        
    - Build up to larger features gradually  
        逐步构建更大功能
        
2. **Stay modular 保持模块化**
    
    - Break everything into small, focused files  
        将所有内容分解为小而专注的文件
        
    - Maintain clear interfaces between components  
        在组件之间保持清晰的接口
        
    - Document your module boundaries  
        记录模块边界
        
3. **Trust your experience 相信你的经验**
    
    - Use AI to accelerate, not replace, your judgment  
        利用 AI 加速而非替代你的判断
        
    - Question generated code that feels wrong  
        质疑那些让你感觉不对的生成代码
        
    - Maintain your engineering standards  
        保持你的工程标准