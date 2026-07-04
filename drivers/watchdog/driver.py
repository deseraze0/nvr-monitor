from watchdog.observers import Observer

from core.event_bus import EventBus
from drivers.watchdog.handler import WatchdogHandler


class WatchdogDriver:
    def __init__(self, path: str, event_bus: EventBus):
        self.path = path
        self.observer = Observer()
        self.handler = WatchdogHandler(event_bus)

    def start(self):
        self.observer.schedule(
            self.handler,
            self.path,
            recursive=False,
        )

        self.observer.start()

        print(f"👀 Watchdog следит за папкой: {self.path}")

    def stop(self):
        self.observer.stop()
        self.observer.join()