---
title: squid-cache 配置域名白名单
date created: 2023-12-27 20:13
date modified: 2024-08-16 11:50
slug: squid-cache-domain-whitelist
tags:
  - Area/RD/运维
---

1. 配置==必须==写在 `#  TAG: http_access` 之后, 下一个TAG之前
2. 先用 `acl` 命令定义一组域名 `acl allowed_domains dstdomain .weixin.qq.com baidu.com`
3. 放行刚刚定义的acl `http_access allow allowed_domains`
4. deny 拒绝其他所有 `http_access deny all`

```conf
#  TAG: http_access
#       Allowing or Denying access based on defined access lists
#
#       To allow or deny a message received on an HTTP, HTTPS, or FTP port:
#       http_access allow|deny [!]aclname ...
#
#       NOTE on default values:
#
#       If there are no "access" lines present, the default is to deny
#       the request.
#
#       If none of the "access" lines cause a match, the default is the
#       opposite of the last line in the list.  If the last line was
#       deny, the default is allow.  Conversely, if the last line
#       is allow, the default will be deny.  For these reasons, it is a
#       good idea to have an "deny all" entry at the end of your access
#       lists to avoid potential confusion.
#
#       This clause supports both fast and slow acl types.
#       See http://wiki.squid-cache.org/SquidFaq/SquidAcl for details.
#
#Default:
# Deny, unless rules exist in squid.conf.
#

#
# Recommended minimum Access Permission configuration:
#
# Deny requests to certain unsafe ports
# http_access deny !Safe_ports

# Deny CONNECT to other than secure SSL ports
# http_access deny CONNECT !SSL_ports

# Only allow cachemgr access from localhost
# http_access allow localhost manager
# http_access deny manager

# We strongly recommend the following be uncommented to protect innocent
# web applications running on the proxy server who think the only
# one who can access services on "localhost" is a local user
#http_access deny to_localhost

#
# INSERT YOUR OWN RULE(S) HERE TO ALLOW ACCESS FROM YOUR CLIENTS
#

# Example rule allowing access from your local networks.
# Adapt localnet in the ACL section to list your (internal) IP networks
# from where browsing should be allowed
#http_access allow localnet
# http_access allow localhost

acl allowed_domains dstdomain .weixin.qq.com baidu.com

http_access allow allowed_domains

# And finally deny all other access to this proxy
http_access deny all

```