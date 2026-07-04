from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from database.database import Base


class EventModel(Base):
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(String, primary_key=True)

    timestamp: Mapped[datetime] = mapped_column(DateTime)

    driver: Mapped[str] = mapped_column(String)

    recorder: Mapped[str] = mapped_column(String)

    camera_id: Mapped[int] = mapped_column(Integer)

    camera_name: Mapped[str] = mapped_column(String)

    event_type: Mapped[str] = mapped_column(String)

    severity: Mapped[str] = mapped_column(String)

    message: Mapped[str] = mapped_column(String)

    snapshot: Mapped[str | None] = mapped_column(String, nullable=True)

    video: Mapped[str | None] = mapped_column(String, nullable=True)