---
title: AI写代码经验分享：GitHub Copilot
date created: 2024-01-18 20:27
date modified: 2024-05-22 19:33
slug: ai-code-experience-share-github-copilot
---
#兴趣/AIGC 

个人一点AI写代码的经验，抛砖引玉，供大家参考。

大家应该看过有牛人用GPT4多模态写代码。他用纸画了一个草图，然后用AI很多轮操作后，给出了一个完整的前端项目。这很cool。但说实话，这种“写代码”不具备现实意义。因为你无法在一张纸上涵盖项目的所有细节。
哪怕AI工具是假的，背后其实有一群资深架构师，他们也需要一份完整的需求文档加上高精度原型图才能做出来。
我们现在不要对AI抱这么大的期望。它能为我们熟悉的某一个工作环节，提升一些效率就很好了。

Github copilot 解决了编写代码时的一些重复性工作。
这里的编写代码指的是在已经有思路、有设计的前提下，给它足够的提示，它就能如你所想，简化你的代码编写。这样就可以达到提升效率、少查文档、延长键盘寿命的效果。

Github copilot 的交互非常丝滑。编写代码过程中，自动就会出现补全。编写提示词可以自然融入编码过程。
而且 Github copilot 的交互很有规律。使用一段时间后开发者可以预料什么时候应该停顿, 给它一点反应时间；也能主动按一定规律写代码，给它更好的提示词，AI就会反馈更好的效果。

Github copilot 速度快。只要网络环境稳定，一般能在1s，大段代码能在3s内响应。与使用GPT-4的Jetbrains AI Assistant相比, 质量会差一点点。
对比质量好与速度快，我个人更喜欢速度快。首先生成慢会打断节奏，影响心流；而且生成的再好，也要开发者最后进行review，而快速生成有利于快速修改。

下面给几个我常用场景

1.文本结构化 纯文本 to schema
2.起变量名
3.代码补全 写接口签名