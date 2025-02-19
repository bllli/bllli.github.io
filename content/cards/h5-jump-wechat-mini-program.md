---
title: H5跳转微信小程序
date created: 2024-11-20 10:23
date modified: 2024-11-22 17:53
tags:
  - Area/RD/踩坑经验/微信
slug: h5-jump-wechat-mini-program
---


https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/url-scheme.html

https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/url-link.html

url-schema 在部分安卓手机上不能用， 而 url-link 可以。

需要从服务端调用微信的接口，这要用到小程序的APPID/SK 换到  access_token，传入小程序页面链接等参数，收到一个链接

这个链接能够跳转到APPID对应的微信小程序

他们都能接收一个拼接参数，拼接参数需要urlencode，其上限为 256字节

小程序接收到此参数是时已经 url decode 过的