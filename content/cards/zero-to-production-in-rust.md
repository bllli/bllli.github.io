---
title: 📚 zero to production in rust
date created: 2024-12-04 10:24
date modified: 2024-12-10 10:46
slug: zero-to-production-in-rust
tags:
  - Area/RD/rust
  - Resource/学习资料
---


官方网站

https://www.zero2prod.com/index.html?country=China&discount_code=SEA60

---

相关项目

https://actix.rs/

https://github.com/juhaku/utoipa OpenAPI document generate For Rust


---

## 相关讨论

https://blog.erodriguez.de/dependency-management-fatigue-or-why-i-forever-ditched-react-for-go-htmx-templ/

  
I recently shipped a project [0] with a very similar tech stack: Axum + HTMX + Askama. It’s still in beta but it’s incredible how far you can get with just html, css and less than 20 lines of js. Also, can’t beat the beauty of putting a single binary in a systemd service and have your entire frontend + backend ready to go.  
我最近发布了一个项目[0]，采用了非常相似的技术栈：Axum + HTMX + Askama。虽然它仍处于测试阶段，但仅凭 HTML、CSS 和不到 20 行的 JavaScript 就能实现如此多的功能，实在令人惊叹。此外，将一个单一的二进制文件放入 systemd 服务中，就能让整个前端和后端准备就绪，这种简洁之美无可匹敌。

The only downside that I see is that the binary gets big pretty fast, especially with Askama which basically is a templating engine like Tera but pulls templates at compile time in the binary so you don’t have to copy templates around on your server.  
我唯一看到的缺点是二进制文件增长得相当快，尤其是使用 Askama 时，它基本上是一个模板引擎，类似于 Tera，但在编译时将模板拉入二进制文件中，因此你不必在服务器上四处复制模板。

I have not worked with SSR a lot before but it seems it’s harder to cache pages too.  
我之前没有太多使用 SSR 的经验，但似乎缓存页面也变得更困难了。

[0]: [https://ulry.app](https://ulry.app/)

---

I'd love to read some blog posts on your process. Actix never struck me as super easy, at least when I checked it some 2-3 years ago.  
我很想读一些关于你开发过程的博客文章。Actix 从未让我觉得特别简单，至少在我两三年前查看时是这样。


---

I'd highly recommend reading some articles by Luca Palmieri[1], or even buying his book[2]. Although I didn't learn this stack by working through his book, whenever I had questions through the years, my searches usually led me to his articles which are often excerpts from the larger book.  
我强烈推荐阅读 Luca Palmieri 的一些文章[1]，甚至购买他的书[2]。虽然我并非通过他的书来学习这个技术栈，但多年来每当遇到疑问时，我的搜索结果常常指向他的文章，这些文章通常摘自那本更全面的书籍。

The high level of API stability and lack of churn in the Actix ecosystem makes the book a particularly good investment for someone looking to settle on this stack in my opinion. In keeping with the topic of this submission, I doubt I'd be comfortable spending money on a similar book about building web apps with React.  
Actix 生态系统中 API 的高稳定性及低变动性，使得这本书对于那些希望在此技术栈上稳定下来的开发者来说，是一笔特别值得的投资，依我之见。与本次提交的主题相符，我恐怕不会愿意花钱购买一本关于使用 React 构建 Web 应用的类似书籍。

[1]: [https://www.lpalmieri.com/posts/2020-08-09-zero-to-productio...](https://www.lpalmieri.com/posts/2020-08-09-zero-to-production-3-how-to-bootstrap-a-new-rust-web-api-from-scratch)

[2]: [https://www.zero2prod.com](https://www.zero2prod.com/)

---