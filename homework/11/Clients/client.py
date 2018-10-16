import asyncio
import aiohttp
from random import randint
n = 1000

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://127.0.0.1:5000/data')
        await asyncio.sleep(randint(1, 10))
        print(html)

async def cycle(n):
    tasks = [asyncio.ensure_future(main()) for i in range(n)]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cycle(n))

