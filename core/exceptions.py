class NVRMonitorError(Exception):
    """Базовое исключение проекта."""


class DriverError(NVRMonitorError):
    """Ошибка драйвера."""


class TelegramError(NVRMonitorError):
    """Ошибка Telegram."""


class DatabaseError(NVRMonitorError):
    """Ошибка базы данных."""


class ConfigError(NVRMonitorError):
    """Ошибка конфигурации."""