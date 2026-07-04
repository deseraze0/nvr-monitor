import asyncio

from core.event_bus import EventBus

from telegram.service import TelegramService
from database.service import DatabaseService
from database.database import init_database

from drivers.watchdog.driver import WatchdogDriver


WATCH_FOLDER = r"C:\Users\deser\Downloads"


async def main():

    await init_database()

    bus = EventBus()

    bus.subscribe(DatabaseService().handle_event)
    bus.subscribe(TelegramService().handle_event)

    driver = WatchdogDriver(WATCH_FOLDER, bus)

    driver.start()

    print("Ожидание новых файлов...")

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        driver.stop()


asyncio.run(main())