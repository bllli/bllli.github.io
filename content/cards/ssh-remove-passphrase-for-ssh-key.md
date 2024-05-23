---
title: ssh remove the passphrase for the ssh key
date created: 2023-12-27 14:48
date modified: 2024-05-23 21:32
slug: ssh-remove-passphrase-for-ssh-key
---
#Area/RD/运维/linux  

为一个 ssk key 移除密码

```
$ ssh-keygen -p
```

This will then prompt you to enter the keyfile location, the old passphrase, and the new passphrase (which can be left blank to have no passphrase).


https://stackoverflow.com/questions/112396/how-do-i-remove-the-passphrase-for-the-ssh-key-without-having-to-create-a-new-ke
