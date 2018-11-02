---
layout: article
title: CentOS7 firewalld 防火墙配置
key: centos7-firewalld
tags:
  Linux
---
网上有的是，就是格式有点不舒服。整理一份自己用。
<!--more-->

# firewalld

常用: 查看开放端口 / 永久开放指定端口 / reload使开放操作生效
```
firewall-cmd --zone=public --list-ports
firewall-cmd --zone=public --add-port=<port>/tcp --permanent
firewall-cmd --reload
```

其他命令
```
yum install firewalld firewalld-config

systemctl start firewalld  # 启动防火墙
systemctl stop firewalld  # 禁用防火墙
systemctl enable firewalld  # 设置开机启动
systemctl disable firewalld  # 停止并禁用开机启动
systemctl status firewalld  # 查看状态

firewall-cmd --state  # 查看状态
firewall-cmd --reload  # 重启防火墙

firewall-cmd --get-active-zones  # 查看区域信息
firewall-cmd --get-zone-of-interface=eth0  # 查看指定接口所属区域信息
```

## Thanks
[Centos防火墙设置与端口开放的方法](https://blog.csdn.net/u011846257/article/details/54707864)
