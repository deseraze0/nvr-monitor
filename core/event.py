from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import uuid4


class EventType(Enum):
    MOTION = "motion"
    HUMAN = "human"
    FACE = "face"
    LINE_CROSSING = "line_crossing"
    INTRUSION = "intrusion"
    VIDEO_LOSS = "video_loss"
    DISK_ERROR = "disk_error"
    VISITOR_COUNT = "visitor_count"
    MASK = "mask"
    LICENSE_PLATE = "license_plate"
    UNKNOWN = "unknown"


class Severity(Enum):
    INFO = "info"
    WARNING = "warning"
    ALARM = "alarm"
    CRITICAL = "critical"


@dataclass(slots=True)
class Event:
    driver: str
    recorder: str
    camera_id: int
    camera_name: str

    event_type: EventType
    severity: Severity

    message: str = ""

    snapshot: str | None = None
    video: str | None = None

    metadata: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)