import time
import asyncio


def job(t):
    print('Start job', t)
    time.sleep(t)
    print('Job takes', t, 'seconds')


def execute_jobs():
    [job(t) for t in range(1, 3)]


async def async_job(t):
    print('Start job', t)
    await asyncio.sleep(t)
    print('Job takes', t, 'seconds')


async def async_execute_jobs(loop):
    tasks = [loop.create_task(job(t)) for t in range(1, 3)]
    await asyncio.wait(tasks)


def main():
    # Non asyncio
    start = time.time()
    execute_jobs()
    end = time.time()
    total_time = end - start
    print('\nNon Asyncio Time:', total_time, '\n')

    # asyncio
    start = time.time()
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(async_execute_jobs(event_loop))
    event_loop.close()
    end = time.time()
    total_time = end - start
    print('\nAsyncio Time:', total_time, '\n')


if __name__ == '__main__':
    main()
