---
tags:
  - Area/RD/运维/linux
title: ssh 指定使用哪个 private key
date created: 2023-12-27 00:33
date modified: 2024-08-16 11:50
slug: specify-private-key-ssh
---
  

```
ssh -i ~/.ssh/id_rsa-2308 'root@114.96.81.75'
```

[How to disable ssh password login on Linux to increase security - nixCraft](https://www.cyberciti.biz/faq/how-to-disable-ssh-password-login-on-linux/)

```
ssh-copy-id -f -i hostkey.rsa.pub user@target
```
