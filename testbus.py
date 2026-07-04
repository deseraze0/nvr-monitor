import asyncio

from core.event import Event, EventType, Severity
from core.event_bus import EventBus


async def telegram_handler(event):
    print(f"[Telegram] {event.camera_name}: {event.message}")


async def database_handler(event):
    print(f"[Database] Сохранил {event.id}")


async def main():

    bus = EventBus()

    bus.subscribe(telegram_handler)
    bus.subscribe(database_handler)

    event = Event(
        driver="watchdog",
        recorder="Office",
        camera_id=1,
        camera_name="Главный вход",
        event_type=EventType.HUMAN,
        severity=Severity.ALARM,
        message="Обнаружен человек",
    )

    await bus.publish(event)


asyncio.run(main())