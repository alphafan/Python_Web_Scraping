import aiohttp
import requests
import time
import asyncio

URL = 'https://www.youtube.com'


# Normal Scrape

def normal():
    for _ in range(2):
        r = requests.get(URL)
        url = r.url
        print(url)


t1 = time.time()
normal()
print("Normal total time:", time.time()-t1)


# Asyncio Scrape

async def job(sess):
    resp = await sess.get(URL)
    return str(resp.url)


async def main(loop):
    async with aiohttp.ClientSession() as sess:
        tasks = [loop.create_task(job(sess)) for _ in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        for r in finished:
            print(r.result())


start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
end = time.time()
print('Asyncio Time:', end-start)
