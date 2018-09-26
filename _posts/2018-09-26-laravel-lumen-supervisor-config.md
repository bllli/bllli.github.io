---
layout: article
title: 为laravel/lumen queue 配置 supervisor 
key: lumen_supervisor_config
tags:
  工具
  Linux
---
近期工作中使用了
laravel框架中的队列服务,需要运行队列处理器
```php /path/to/artisan queue:work --tries 3``` 命令

测试环境部署时需要：
  - 终止原有queue:work命令
  - 开启新queue:work命令

依照[laravel教程](https://laravel-china.org/docs/laravel/5.6/queues/1395#supervisor-configuration)
推荐使用进程管理工具 supervisor

## Supervisor 安装
```shell
yum install supervisor  # centos
sudo apt-get install supervisor  # ubuntu
```

supervisord 是进程管理的服务端，常驻进程辅助干活  
supervisorctl 是客户端，用来执行查看、加载等命令

## Supervisor 配置
生成配置文件
```
echo_supervisord_conf > /etc/supervisord.conf
```
编辑配置文件
```
vim /etc/supervisord.conf
```
配置文件中配置除了最后两行，使用默认的就行。vim中使用G把光标跳到文件末尾，将最后一行修改为如下。

```
# file: /etc/supervisord.conf
...
[include]
files = /etc/supervisor/*.conf
```
创建文件夹
```
mkdir -p /etc/supervisor/
```
创建queue work启动脚本
```
vim /etc/supervisor/lumen_worker.conf
```
lumen_worker.conf 文件内容 注意修改项目artisan文件路径
```
[program:lumen_worker]
process_name=%(program_name)s_%(process_num)02d
command=php /path/to/artisan queue:listen --tries 3 --sleep 3
autostart=true
autorestart=true
user=root
numprocs=1
redirect_stderr=true
stdout_logfile=/tmp/lumen_worker.log
```

## 启动 supervisor
```
supervisord  
# 启动supervisord服务，默认使用/etc/supervisord.conf配置文件。
# 如果报错Error: Another program is already listening on a port that one of our HTTP servers is configured to use.说明已经启动，继续即可。

supervisorctl reload  # 重启 supervisord
supervisorctl reread  # 重新读取配置文件 supervisord
supervisorctl start lumen_worker:*  # 启动lumen_worker服务

supervisorctl restart lumen_worker:*  # 重启lumen_worker服务
```

启动后查看一下运行状态 
```
supervisorctl status
```
应该能看到lumen_worker处于RUNNING状态：
```
[root@X /etc/supervisor]# supervisorctl status
lumen_worker:lumen_worker_00     RUNNING   pid 19317, uptime 0:01:49
```

## Thanks
[Supervisord管理进程实践](https://thief.one/2018/06/01/1/)  
[Supervisor安装与配置（Linux/Unix进程管理工具）](https://blog.csdn.net/xyang81/article/details/51555473)  
[laravel-china](https://laravel-china.org/docs/laravel/5.6/queues/1395#e45763)
