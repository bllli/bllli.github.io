---
title: 获取服务器公网 ip 地址
date created: 2024-06-04 11:20
date modified: 2024-08-16 11:50
tags:
  - Area/RD/运维/linux
slug: get-server-public-ip-address
---
 


```bash
curl 3.0.3.0
curl ip.fm
```


https://www.ipify.org/ 也行


大佬整理的 https://hostloc.com/thread-954782-1-1.html

```
curl -6 https://ifconfig.co
curl -4 https://ifconfig.co
curl -6 https://ipv6.icanhazip.com
curl -4 https://ipv4.icanhazip.com
curl -6 https://ifconfig.io
curl -4 https://ifconfig.io
curl -6 https://api.myip.com
curl -4 https://api.myip.com
curl -6 https://cloudflare.com/cdn-cgi/trace
curl -4 https://cloudflare.com/cdn-cgi/trace
curl -6 https://ip.fht.im
curl -4 https://ip.fht.im
curl -6 https://bot.whatismyipaddress.com
curl -4 https://bot.whatismyipaddress.com
curl -6 https://www.jsonip.com
curl -4 https://www.jsonip.com
curl -6 https://www.trackip.net/ip
curl -4 https://www.trackip.net/ip
curl -6 https://www.trackip.net/ip?json
curl -4 https://www.trackip.net/ip?json
curl -6 ip.sb
curl -4 ip.sb
dig -6 TXT +short o-o.myaddr.l.google.com @ns1.google.com
dig -4 TXT +short o-o.myaddr.l.google.com @ns1.google.com
dig -6 -t aaaa +short myip.opendns.com @resolver1.opendns.com
dig -4 -t a +short myip.opendns.com @resolver1.opendns.com
telnet ipv6.telnetmyip.com
telnet ipv4.telnetmyip.com
telnet -6 telnetmyip.com
telnet -4 telnetmyip.com
ssh -6 sshmyip.com
ssh -4 sshmyip.com

curl -4 https://ip.threep.top
curl -4 https://ip.fm
curl -4 https://cip.cc
curl -4 https://myip.ipip.net
curl -4 https://myip.biturl.top
curl -4 https://checkip.amazonaws.com
curl -4 https://httpbin.org/ip
curl -4 https://pv.sohu.com/cityjson
curl -4 "https://api.ipify.org?format=json"
curl -4 https://lerry.me/ip
curl -4 https://xabc.io/p
curl -4 https://api.akkariin.com:24443/getip/
curl -4 https://ipinfo.io/ip
curl -4 https://ifconfig.me/ip
curl -4 https://ipgrab.io
curl -4 https://myexternalip.com/raw
curl -4k https://whatismyip.akamai.com
curl -4 checkip.dyndns.com
curl -4 checkip.dyndns.org
```