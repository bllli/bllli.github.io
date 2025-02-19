---
title: '解决 cursor "Too many free trial accounts used on this machine"'
date created: 2024-12-10 17:57
date modified: 2024-12-12 10:29
tags:
  - 兴趣/AIGC/AI写代码
slug: fix-cursor-too-many-free-trial-accounts-used-on-this-machine
---
这台电脑上使用了太多免费账号了，需要替换机器码，这样就能绕过 corsor 的检查。

cursor 将机器码写到了一个本地 json 文件。这一招防君子不防小人。我之前做机器码是每次启动时读取 CPU / 显卡 / 网卡等设备的ID计算出机器码，一直放在内存，这样破解概率会小很多。

---

## macos 

https://github.com/fly8888/cursor_machine_id

--- 

source: https://blog.liurb.org/2024/12/07/change_cursor_machine_id/
