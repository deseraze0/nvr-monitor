from core.event import Event
from database.repository import EventRepository


class DatabaseService:
    def __init__(self) -> None:
        self.repository = EventRepository()

    async def handle_event(self, event: Event) -> None:
        await self.repository.save(event)