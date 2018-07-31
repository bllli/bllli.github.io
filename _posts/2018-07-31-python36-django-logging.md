---
layout: article
title: Django2 + Python3.6 + Logging 打中文log
key: python36_django_logging
tags:
  Django
  Python
---

记录一下在Python3.6下使用Django2.0使用Logging时遇到的坑

<!--more-->

只需要在handler中加上``'encoding': 'utf-8'``就行了

```Python3
LOGGING = {
    ...
    'handlers': {
        'file_dj': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/tmp/{}_dj.log'.format(PROJECT_NAME),
            'encoding': 'utf-8',
            'formatter': 'normal',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/{}_debug.log'.format(PROJECT_NAME),
            'encoding': 'utf-8',
            'formatter': 'normal',
        },
    }
    ...
}

```

