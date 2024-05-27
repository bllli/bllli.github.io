---
title: 将安卓手机的屏幕投射到电脑上 scrcpy
date created: 2024-04-03 14:01
date modified: 2024-05-27 18:37
slug: project-android-phone-screen-to-computer-scrcpy
---

#Resource/tools 

https://github.com/Genymobile/scrcpy/tree/master

## Mac 安装

```
# step 1. 科学上网

# step 2. 安装brew 
# (科学上网状态下)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# step 3. 安装 scrcpy

brew install scrcpy
brew install android-platform-tools

# step 4.
# (不科学上网状态下) 终端执行 
scrcpy
```

## 使用 

现将手机设置为adb调试模式
多次点击版本号打开开发者模式
这个具体看手机型号

```
1. 用数据线连接手机和电脑
2. 在mac打开终端app (terminal)
3. 输入 scrcpy 回车, 
    也可以按⬆️ (找到上一条命令) 找到 scrcpy 再按回车
```