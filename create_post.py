#!/usr/local/bin/python3.7

import os
import sys
from datetime import datetime

# 2018-07-31-python36-django-logging.md

if __name__ == '__main__':
    if not os.path.exists("_posts"):
        raise EnvironmentError("我这是在哪儿?")

    if len(sys.argv) < 2:
        raise Exception("Usage: python3 create_post.py <post_key> <post_title>")

    post_key = sys.argv[1]
    post_title = sys.argv[2]

    today = datetime.now().date()
    post_filename = f'_posts/{today.year}-{today.month}-{today.day}-{post_key}.md'

    if os.path.isfile(post_filename):
        raise Exception("post_filename exists")

    # todo: check key

    with open(post_filename, 'w') as f:
        f.write(f"""---
layout: article
title: {post_title}
key: {post_key} 
tags:
  <todo>
---

<!--more-->

""")
    print('vim ' + post_filename)
