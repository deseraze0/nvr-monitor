import asyncio
from watchdog.events import FileSystemEventHandler

from core.event_bus import EventBus
from drivers.watchdog.parser import WatchdogParser


class WatchdogHandler(FileSystemEventHandler):
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self.parser = WatchdogParser()

    def on_created(self, event):
        if event.is_directory:
            return

        parsed_event = self.parser.parse(event.src_path)

        if parsed_event is None:
            return

        try:
            loop = asyncio.get_running_loop()
            loop.create_task(self.event_bus.publish(parsed_event))
        except RuntimeError:
            asyncio.run(self.event_bus.publish(parsed_event))