## Python aiohttp Scrape Website Pages

```python
# Asyncio Scrape

import aiohttp
import asyncio

URL = 'https://www.youtube.com/'


async def job(sess):
    resp = await sess.get(URL)
    return str(resp.url)


async def main(loop):
    async with aiohttp.ClientSession() as sess:
        tasks = [loop.create_task(job(sess)) for _ in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        for r in finished:
            print(r.result())
            

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
```