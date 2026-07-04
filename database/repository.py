from sqlalchemy import select

from core.event import Event
from database.database import SessionLocal
from database.models import EventModel


class EventRepository:

    async def save(self, event: Event):

        async with SessionLocal() as session:

            db_event = EventModel(
                id=event.id,
                timestamp=event.timestamp,
                driver=event.driver,
                recorder=event.recorder,
                camera_id=event.camera_id,
                camera_name=event.camera_name,
                event_type=event.event_type.value,
                severity=event.severity.value,
                message=event.message,
                snapshot=event.snapshot,
                video=event.video,
            )

            session.add(db_event)

            await session.commit()

    async def get_last(self, limit: int = 20):

        async with SessionLocal() as session:

            result = await session.execute(
                select(EventModel).limit(limit)
            )

            return result.scalars().all()