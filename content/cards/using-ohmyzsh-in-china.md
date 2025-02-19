---
title: 国内网络使用 ohmyzsh
date created: 2024-12-18 10:20
date modified: 2024-12-30 14:34
slug: using-ohmyzsh-in-china
tags:
  - Area/RD/GFW
  - Area/RD/运维
  - todo
---

当服务不能访问 github 时

###   安装

在本地克隆后获取安装脚本。

```

git clone https://mirrors.tuna.tsinghua.edu.cn/git/ohmyzsh.git
cd ohmyzsh/tools
REMOTE=https://mirrors.tuna.tsinghua.edu.cn/git/ohmyzsh.git sh install.sh
```

### 切换已有 ohmyzsh 至镜像源

```
git -C $ZSH remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/ohmyzsh.git
git -C $ZSH pull
```


## Source
https://mirrors.tuna.tsinghua.edu.cn/help/ohmyzsh.git/


## 切换到 zsh 

```bash
chsh -s $(which zsh)
```


zshrc
```
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)
```