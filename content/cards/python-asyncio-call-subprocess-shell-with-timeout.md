---
title: python asyncio call subprocess_shell with timeout
date created: 2024-04-11 16:26
date modified: 2024-05-23 21:04
slug: python-asyncio-call-subprocess-shell-with-timeout
---

#Area/RD/backend/python 

```python
import asyncio
import logging
import uuid


async def call(command, timeout=300):
    command_excute_id = uuid.uuid4().hex
    process = await asyncio.create_subprocess_shell(
        command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    async def kill_proc():
        await asyncio.sleep(timeout)
        process.kill()
        logging.info("[%s] process timeout, killed.", command_excute_id)
        return await process.communicate()

    killer = asyncio.create_task(kill_proc())

    stdout, stderr = "", ""
    await process.wait()
    stdout, stderr = await process.communicate()

    if not killer.done():
        killer.cancel()
    else:
        stdout, stderr = killer.result()

    returncode = process.returncode
    if returncode != 0:
        logging.error("[%s] command failed: %s", command_excute_id, command)
        logging.error("[%s] stderr: %s", command_excute_id, stderr)
        logging.error("[%s] stdout: %s", command_excute_id, stdout)

    return returncode, stdout, stderr


async def main():
    r = await call("echo 'hello' && sleep 0.4 && echo 'fine!'", timeout=1)
    print("info", r)


if __name__ == "__main__":
    asyncio.run(main())


```