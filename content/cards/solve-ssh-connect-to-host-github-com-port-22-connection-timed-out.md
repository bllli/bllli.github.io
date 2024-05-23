---
title: 解决 ssh connect to host github.com port 22 Connection timed out
date created: 2024-01-18 22:43
date modified: 2024-05-23 21:13
slug: solve-ssh-connect-to-host-github-com-port-22-connection-timed-out
---
#Area/RD/运维/linux 
#Area/RD/科学上网 

[解决 ssh: connect to host github.com port 22: Connection timed out - the_blog - SegmentFault 思否](https://segmentfault.com/a/1190000040896781)

如果你电脑上的git能在大部分地方进行同步，但是在某处地方的网络下无法同步，并且运行`git pull`或`git push`长久没有反映，最后出现`ssh: connect to host github.com port 22: Connection timed out`，很可能是你的网络供应商（比如广电网）在出口防火墙上屏蔽了22端口，这意味着你将无法访问其他主机的22端口。

对此，github提供了一种解决方案，允许你使用443端口进行ssh连接，因为443端口是访问https网站所必须的，大部分防火墙都会允许通过，但如果使用代理服务器可能产生干扰。如果连443端口都被屏蔽，那你应该无法浏览这篇文章。

运行这段命令，看看是否有成功提示，如果成功，则可以使用这个解决方案。

ssh -T -p 443 git@ssh.github.com

简单地配置一下，让你每次ssh连接github都通过443端口。如果你使用Linux，在`~/.ssh/config`内，添加这些内容，指明ssh连接`git@github.com`或`git@ssh.github.com`走443端口。

Host github.com
Hostname ssh.github.com
Port 443
User git

需要注意的是，**假如你的电脑上拥有多个github账户**，你可能事先修改过ssh的配置文件，你可能会将配置文件修改成这样子。

# For the account1
Host github_account1
HostName ssh.github.com
PreferredAuthentications publickey
Port 443
User git
IdentityFile ~/.ssh/id_rsa_account1

# For the account2
Host github_account2
HostName ssh.github.com
PreferredAuthentications publickey
Port 443
User git
IdentityFile ~/.ssh/id_rsa_account2

相比于普通只配置一个账户的用户，多账户用户在设置远程仓库连接时，项目内的git配置文件也要修改，往往设置成这个样子。

# .git/config
[remote "origin"]
    url = git@github_account1:account1/my_repo.git

你将通过配置文件中设置的`Host`别名`github_account1`代替`github.com`访问github，这意味着，如果你想要进行进行git clone操作，也应该通过别名访问，否则无法走443端口。假如你想clone `git@github.com:torvalds/linux.git`，你应该将链接修改为`git@你设置的别名:torvalds/linux.git`。或者是，额外在配置文件里加上。这样就能直接`git clone git@github.com:torvalds/linux.git`了。

# Just for clone
Host github.com
HostName ssh.github.com
Port 443
User git

## 参考

- [x] [Using SSH over the HTTPS port](https://link.segmentfault.com/?enc=ks0AUrOJStsReDq7ImwTmQ%3D%3D.uPRj2B48K9gPtYEzSBV5GztggCF7rSzHnsU42AP9FUKy3%2FIelT3PmwZwD7zcTbqPgPt4DvXlQSwWSv2sPXUs5y1q9U8SolG8sTf3I6HszbUYV2wWKm971e0mX18VSqHf)
- [x] [ssh: connect to host github.com port 22: Connection timed out](https://link.segmentfault.com/?enc=ZAoZa7k0LGi0H8lloEFUnQ%3D%3D.p%2F8x4vEFmw16VCTWiqd7u%2BonLcb8qKQoRswORNn5%2B%2BoBqkTfvxcT7WiLEC16xpgf%2F%2BeELJ4r2VASQnPYbb%2F2yqFwWtzJqG8tRnfi%2F7aDBCElQZsb99o6S14GLuVq1bDkXbHEi0IPNKxwNvfIbNxh9Q%3D%3D)