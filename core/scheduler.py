import asyncio


class Scheduler:

    async def every(self, seconds: int, func):

        while True:
            await func()
            await asyncio.sleep(seconds)