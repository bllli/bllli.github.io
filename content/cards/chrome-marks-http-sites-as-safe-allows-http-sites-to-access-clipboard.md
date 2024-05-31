---
title: Chrome 将 http 网站标记为安全，允许 http 网站访问剪切板
date created: 2024-05-30 17:48
date modified: 2024-05-31 14:22
slug: chrome-marks-http-sites-as-safe-allows-http-sites-to-access-clipboard
---

有个内网网站，网站上有个按钮，点击会向写剪切板写数据。

但 Chrome 认为 http 网站不安全，会限制其权限，包括剪切板权限。而这个剪切板权限我们又不能控制。

thanks https://stackoverflow.com/questions/64060102/how-to-change-the-site-setting-of-unsecuredhttp-websites-on-chrome

可以强制将此网站设置标记为安全

```

打开 chrome://flags/ 
( edge://flags )

查找 #unsafely-treat-insecure-origin-as-secure
改为 “enabled”

在输入框填写 http://192.168.1.1:8080

```

