---
title: python block io 阻塞 eventloop 实例
date created: 2024-04-11 16:25
date modified: 2024-05-23 21:05
slug: python-block-io-eventloop-example
---

#Area/RD/backend/python 

```python
import asyncio

import aiohttp
import requests

counter = 0


class Flag:
    def __init__(self):
        self.flag = False


big_file_url = "https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2023-06/Digital_News_Report_2023.pdf"


async def async_req():
    async with aiohttp.ClientSession() as session:
        async with session.get(big_file_url) as response:
            print("!!!!!", response.status)


def block_req():
    resp = requests.get(big_file_url)
    print("!!!!!!", resp.status_code)


async def tick(flag: Flag):
    while not flag.flag:
        global counter
        counter += 1
        print("tick", counter)
        await asyncio.sleep(0.1)


async def main():
    flag = Flag()
    task = asyncio.create_task(tick(flag))

    await asyncio.sleep(1)
    block_req()
    # await async_req()
    print("awake")
    await asyncio.sleep(1)
    print("set flag")
    flag.flag = True
    await task


asyncio.run(main())

```