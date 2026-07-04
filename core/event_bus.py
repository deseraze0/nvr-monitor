import asyncio
from collections.abc import Awaitable, Callable

from core.event import Event

EventHandler = Callable[[Event], Awaitable[None]]


class EventBus:
    """
    Центральная шина событий проекта.
    """

    def __init__(self) -> None:
        self._handlers: list[EventHandler] = []

    def subscribe(self, handler: EventHandler) -> None:
        """
        Подписать обработчик на получение событий.
        """
        if handler not in self._handlers:
            self._handlers.append(handler)

    def unsubscribe(self, handler: EventHandler) -> None:
        """
        Отписать обработчик.
        """
        if handler in self._handlers:
            self._handlers.remove(handler)

    async def publish(self, event: Event) -> None:
        """
        Отправить событие всем подписчикам.
        """
        if not self._handlers:
            return

        await asyncio.gather(
            *(handler(event) for handler in self._handlers)
        )