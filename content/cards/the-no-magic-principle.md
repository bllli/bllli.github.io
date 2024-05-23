---
title: The No Magic Principle
date created: 2024-05-16 15:56
date modified: 2024-05-23 21:06
slug: the-no-magic-principle
---

#兴趣/哲学/思维方式

https://blog.s-schoener.com/2017-11-29-no-magic/

I have always been drawn to computers and I like to think that computers shaped most of my thoughts and ideas about philosophy and life in general. One of the key points that make me so fond of computers is what I call the *No Magic Principle*:

> Computers don’t involve magic.

Everything that happens inside a computer follows a strict set of rules that can be understood and can be reasoned about in the abstract. For most everyday programming tasks, it is acceptable to just live and work in this perfect world without caring about its physical implementation. This is pure joy, like swimming in a sea of mathematics.

Unfortunately, humans are notoriously bad at *not* using magical thinking in their reasoning, which is why I find it utmost important to always keep the No Magic Principle in mind when programming (especially when *teaching* other people how to program), hence this blog post. Also, I finally want a place to point to when I am asked what I mean when I start my arguments with *…by no-magic, we know that…* ;)

## Corollaries

The No Magic principle has a few immediate corrolaries:

1. **You can build it.** See that awesome shader effect someone created? That weird webapp? You can dissect it, understand it, and build it yourself. It might take some time, but in principle it is possible. Another statement of this corollary might read *If it is there, it must have been built.* [Relevant XKCD](https://xkcd.com/1741/):![https://xkcd.com/1741/](https://imgs.xkcd.com/comics/work.png)While the general message may seem uplifting, this also implies that every ever so small feature was implemented by someone. In case you are not programming yourself, you may take this moment to appreciate the people that implemented all the undo-systems we always take for granted and the engineer(s?) that built the minimap in StarCraft.
    
2. **Pick your fights.** If something *seems* impossible, there is a good chance it *is* impossible. For example, if you cannot even come up with a slow, inefficient, and stupid algorithm, why would you expect to find an efficient one? I am not saying you shouldn’t try (especially if you are doing research), but choose your battles wisely. Maybe your problem is solvable with a suitable restriction? After all, there [are cases](http://math.andrej.com/2007/09/28/seemingly-impossible-functional-programs/) where the seemingly impossible is possible after all (spoiler: the restriction here is to only consider computable functions – an assumption implicit to most work with computers). But be sceptical and demand proof in such cases.
    
3. **It’s probably your fault.** So your program is crashing. Again. And again. And again. What are the chances of a hardware fault? Pretty slim. Maybe the underlying OS is doing funky things? That is still *pretty unlikely*, but [does come up from time to time](https://blogs.unity3d.com/2016/04/25/debugging-memory-corruption-who-the-hell-writes-2-into-my-stack-2/) (– but do note that the memory corruption issue described in that post is not a bug in the OS but stems from *wrong usage* of system calls). Usually, however, it will be *your code* that is wrong, and you should be prepared for that. I’d like to think that an essential step in learning to program is to accept this and your faults. Especially students should not be embarassed of their mistakes. After all, machines only do what you tell them to do *and that’s the essential feature*. There is no point in blaming the machine; take credit for your mistakes and learn from them (and don’t be too harsh on your colleagues for their inevitable mistakes; it’ll come back to you eventually).
    
4. **Be rational.** Once you have realised that you have planted some terrible bugs into your program, there comes the time to debug your code. I have seen many, many people fail at this specifically: They disregard all common-sense and start tinkering with their program endlessly: *Maybe it won’t crash if I set this flag? Maybe the results are correct if I transpose this matrix before the multiplication? Maybe I should check that this library function used by millions of other users is actually doing the right thing?* This approach of pulling levers and hoping for some miracle to happen is woefully inadequate for computers, i.e. systems that don’t involve magic. Generally, there will be a good reason why your program crashes, *so find that reason*. Understand it. Then fix it. Admittedly, sometimes *it is* the odd bug in some library function, but with established libraries that is rather unlikely. So develop a theory of why your program crashes and test it. Don’t let your brain’s need for magical thinking lead you astray.
    
5. **You can understand it**. Computers can be understood, and that’s an incredible possibility that one should take advantage of. Of course, there is a reasonable level of abstraction that you should aim to maintain. For me, that cutoff is once the physical domain really comes into play: I like abstract systems and my primary concern should not be the physical implementation of such systems. It does not hurt to know the physical limitations of your computer, and once you start talking about clock rates and transfer times you will eventually get there. For example, knowing about cache consistency is helpful (for high performance computing), but knowing about the exact working of transistors less so. Personally, I am skeptical of any code that I couldn’t compile myself, at least roughly. While I don’t think you need to teach undergrads a whole semester of x86 assembly, not exposing them to the lower levels of computing is a crime: Computers are reductionist-machines by design and that should be embraced to drive the point home that your compiler is not a magical tool but something that can be understood in all of its details.


### 无魔法原则

发表于 2017 年 11 月 29 日

我一直被计算机所吸引，并且我喜欢认为计算机塑造了我对哲学和生活的许多想法。让我如此喜欢计算机的一个关键点是我称之为无魔法原则：

计算机不涉及魔法。

计算机内部发生的一切都遵循一套严格的规则，这些规则是可以理解的，可以在抽象层面上进行推理。对于大多数日常编程任务，只需要在这个完美的世界中生活和工作，而不必关心其物理实现。这是一种纯粹的快乐，就像在数学的海洋中游泳。

不幸的是，人类在推理中非常擅长使用魔法思维，这就是为什么我认为在编程时（特别是在教授别人如何编程时）始终牢记无魔法原则是最重要的，因此写了这篇博客。此外，当我以“根据无魔法原则，我们知道……”开头我的论点时，我终于有一个可以指向的地方了。;)

### 推论

无魔法原则有几个直接的推论：

**你可以构建它。** 看到有人创建的那个很棒的着色器效果了吗？那个奇怪的网页应用程序？你可以将其拆解，理解它，然后自己构建。可能需要一些时间，但原则上这是可能的。这个推论的另一个表述可能是“如果它存在，那它一定是被构建出来的”。相关的 XKCD：[https://xkcd.com/1741/](https://xkcd.com/1741/) 虽然一般的信息看起来很鼓舞人心，但这也意味着每一个微小的特性都是由某个人实现的。如果你自己没有编程，你可能会在此时感谢那些实现了我们总是理所当然认为存在的撤销系统和构建星际争霸迷你地图的工程师（们？）。

**选择你的战斗。** 如果某件事看起来不可能，那很有可能它确实不可能。例如，如果你甚至无法提出一个缓慢、低效且愚蠢的算法，为什么你会期望找到一个高效的算法呢？我并不是说你不应该尝试（特别是如果你在做研究），但要明智地选择你的战斗。也许你的问题可以通过适当的限制来解决？毕竟，有些情况下看似不可能的事情实际上是可能的（剧透：这里的限制是只考虑可计算的函数——这是大多数计算机工作中的一个隐含假设）。但在这种情况下要持怀疑态度并要求证明。

**很可能是你的错。** 所以你的程序崩溃了。一次又一次。出现硬件故障的几率有多大？很小。也许底层的操作系统在做奇怪的事情？这仍然不太可能，但确实有时会发生（但请注意，这篇文章中描述的内存损坏问题并不是操作系统的错误，而是源于系统调用的错误使用）。然而，通常情况下，问题出在你的代码上，你应该为此做好准备。我认为学习编程的一个重要步骤是接受这一点并承认自己的错误。尤其是学生，不应该为自己的错误感到尴尬。毕竟，机器只会执行你告诉它的操作，而这就是它的基本特征。没有必要责怪机器；为你的错误负责并从中学习（也不要对同事的不可避免的错误太苛刻；这些错误最终也会发生在你身上）。

**要理性。** 一旦你意识到你的程序中存在一些可怕的错误，就该调试你的代码了。我见过很多人在这方面失败：他们忽视所有常识，开始无休止地修修补补他们的程序：如果我设置这个标志，程序可能不会崩溃？如果我在乘法之前转置这个矩阵，结果可能是正确的？我是否应该检查这个被数百万其他用户使用的库函数是否真的做了正确的事情？这种拉动杠杆并希望奇迹发生的方法对于不涉及魔法的计算机系统来说是完全不合适的。一般来说，你的程序崩溃会有一个合理的原因，所以找出那个原因。理解它，然后修复它。诚然，有时确实是某个库函数中的奇怪错误，但对于已建立的库来说，这种情况相当罕见。因此，提出一个关于为什么程序崩溃的理论并进行测试。不要让你的大脑的魔法思维需求误导你。

**你可以理解它。** 计算机是可以理解的，这是一个不可思议的可能性，应该加以利用。当然，你应该努力保持合理的抽象水平。对我来说，一旦物理领域真的开始发挥作用，我就会设定这个界限：我喜欢抽象系统，我的主要关注点不应该是这些系统的物理实现。了解计算机的物理限制并没有坏处，一旦你开始谈论时钟频率和传输时间，你最终会涉及到这些问题。例如，了解缓存一致性对于高性能计算是有帮助的，但了解晶体管的具体工作原理则没那么重要。个人而言，我对任何我不能自己大致编译的代码持怀疑态度。虽然我不认为你需要教本科生一个学期的 x86 汇编，但不让他们接触计算机的低层次是犯罪：计算机是设计上具还原性的机器，这一点应该被接受，以此来强调编译器不是一个神奇的工具，而是可以在其所有细节上理解的东西。