from core.event import Event
from telegram.notifier import TelegramNotifier


class TelegramService:
    def __init__(self) -> None:
        self.notifier = TelegramNotifier()

    async def handle_event(self, event: Event) -> None:
        """
        Обработчик события для EventBus.
        """
        await self.notifier.send_event(event)