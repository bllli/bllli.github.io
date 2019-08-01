---
layout: article
title: 两个celery共用一个redis
key: two_celery_one_redis 
tags:
  Python
  celery
---
为了给公司省下redis的钱(其实是我懒得走申请)，我成功使两个celery服务运行在一台redis上，分别执行互不干扰。
<!--more-->


我使用场景是有多个离线计算服务，需要使用celery执行定时任务。每个离线任务项目均需要一个celery，分别部署互不干扰。

不料两个celery的broker是同一个redis，celeryA的task被celeryB的worker消费了，惊了。

解法1: 用不同的redis db  
问题: 一个redis就16个db

解法2: celery Queue, 把自己的task分配到自己的Queue, 自己的worker只消费自己发的task

目录结构：
```
.
├── celeryconfig.py
├── run.sh
└── main.py
```

celeryconfig.py
```python
from config import TASK_NAME, CELERY_BROKER
from kombu import Queue


BROKER_URL = CELERY_BROKER

CELERY_DEFAULT_QUEUE = TASK_NAME
CELERY_QUEUES = (
    Queue(TASK_NAME, routing_key=TASK_NAME),
)
CELERY_DEFAULT_ROUTING_KEY = TASK_NAME

CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'Asia/Shanghai'
```

main.py
```python
from celery import Celery
from celery.schedules import crontab

celery_app = Celery(TASK_NAME)

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    设置任务定时执行
    see https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
    注意crontab每个参数的默认值均为*
      如 crontab(hour='7') 不是指每天7点执行一次，而是每天七点中的每分钟执行一次
      crontab(hour='7', minute='0') 才是每天七点整执行一次
    """
    # Calls test('hello') every 100 seconds.
    # sender.add_periodic_task(100.0, test.s('hello'), name='add every 100s')

    # 每天凌晨五点执行
    sender.add_periodic_task(
        crontab(hour='5', minute='0'),
        irt_task_main.s(),
    )
    pass

@celery_app.task
def main():
    # todo
    pass
```

run.sh
```shell
celery -A main worker -E --loglevel=info -B -Q [YOUR_TASK_NAME] --config celeryconfig
```

## Thanks
- [https://denibertovic.com/posts/celery-best-practices/](https://denibertovic.com/posts/celery-best-practices/)

