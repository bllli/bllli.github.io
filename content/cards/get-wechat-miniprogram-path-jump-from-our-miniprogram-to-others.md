---
title: 获取微信小程序路径, 以便从我们小程序公众号中跳转到别人的小程序
date created: 2024-04-03 18:11
date modified: 2024-05-23 21:14
slug: get-wechat-miniprogram-path-jump-from-our-miniprogram-to-others
---

#Area/RD/踩坑经验/微信 

功能依据: wx.navigateToMiniProgram 
https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html

我们有appid、路径、路径参数, 就能跳转到其他小程序的页面!

可是我们不知道别人小程序页面的路径和路径参数怎么办呢?

1. 目标小程序的AppID
2. 公众号 文章编辑页 插入小程序
3. 打开你微信号小程序的路径拷贝权限 10分钟有效
4. 拷贝出链接

小技巧: 页面路径可能不用立即更新, 如京东购物的检索结果页面, 这时可以分享小程序 - 从分享的消息中打开小程序 - 如果小程序打开时, 就是搜索结果页 - 且带着你输入的关键字
那么说明此时页面路径就是带关键字的, 可以拷贝了!


## logs

京东健康
wx862d8e26109609cb

pages/searchlist/searchlist.html?name=止咳橘红口服液

pages/product/product.html?venderId=708700&wareId=10092642352107

呼吸道

pages/login/wv-common/wv-common.html?h5_url=https%3A%2F%2Fshop.m.jd.com%2Fshop%2Fintroduce%3FshopId%3D705210%26venderId%3D708700


pages/searchlist/searchlist.html

pages/searchlist/searchlist?name=小鸟快验 呼吸道
