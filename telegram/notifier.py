from aiogram.types import FSInputFile

from core.event import Event
from telegram.bot import bot


class TelegramNotifier:

    async def send_text(self, text: str):

        from core.config import get_config

        config = get_config()

        await bot.send_message(
            chat_id=config.telegram.chat_id,
            text=text,
        )

    async def send_event(self, event: Event):

        text = (
            "🚨 Новое событие\n\n"
            f"Камера: {event.camera_name}\n"
            f"Тип: {event.event_type.value}\n"
            f"Важность: {event.severity.value}\n"
            f"Сообщение: {event.message}"
        )

        await self.send_text(text)

    async def send_photo(self, photo_path: str, caption: str = ""):

        from core.config import get_config

        config = get_config()

        photo = FSInputFile(photo_path)

        await bot.send_photo(
            chat_id=config.telegram.chat_id,
            photo=photo,
            caption=caption,
        )

    async def send_video(self, video_path: str, caption: str = ""):

        from core.config import get_config

        config = get_config()

        video = FSInputFile(video_path)

        await bot.send_video(
            chat_id=config.telegram.chat_id,
            video=video,
            caption=caption,
        )