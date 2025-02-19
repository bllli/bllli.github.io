---
title: 小程序无资质播放视频 通过视频号
date created: 2024-06-26 17:48
date modified: 2024-08-16 11:50
slug: wechat-miniprogram-video-play
tags:
  - Area/RD/踩坑经验/微信
---
 

https://developers.weixin.qq.com/community/develop/doc/00084095ccc0d0327831032df66000?highLine=channel-video

没有视频资质不能用 video 组件。

也不能用channel-video组件

网友评论：

如果没有资质，可以这么做，下列内容是审核人员说的：

小程序中不能出现视频，也不能具备播放能力。channel-video之所以不行，是因为这个组件具备视频播放能力。但是可以在需要播放视频的地方，放一张图片，点击图片，调用wx.openChannelsActivity，跳转到视频号中去播放视频。