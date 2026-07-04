from pathlib import Path

from core.event import Event, EventType, Severity


class WatchdogParser:
    def parse(self, file_path: str) -> Event | None:
        path = Path(file_path)

        if not path.exists():
            return None

        suffix = path.suffix.lower()

        if suffix not in [".jpg", ".jpeg", ".png", ".mp4"]:
            return None

        event_type = (
            EventType.SNAPSHOT
            if suffix in [".jpg", ".jpeg", ".png"]
            else EventType.VIDEO
        )

        return Event(
            driver="watchdog",
            recorder="EasyVMS",
            camera_id=0,
            camera_name="EasyVMS",
            event_type=event_type,
            severity=Severity.INFO,
            message=f"Новый файл: {path.name}",
            snapshot=str(path) if event_type == EventType.SNAPSHOT else None,
            video=str(path) if event_type == EventType.VIDEO else None,
        )