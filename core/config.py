from functools import lru_cache

import yaml
from pydantic import BaseModel


class AppConfig(BaseModel):
    name: str
    debug: bool


class DatabaseConfig(BaseModel):
    url: str


class TelegramConfig(BaseModel):
    token: str
    chat_id: int


class StorageConfig(BaseModel):
    images: str
    videos: str


class LoggingConfig(BaseModel):
    level: str


class DriverConfig(BaseModel):
    enabled: bool


class DriversConfig(BaseModel):
    watchdog: DriverConfig
    xm: DriverConfig
    hikvision: DriverConfig
    dahua: DriverConfig


class Config(BaseModel):
    app: AppConfig
    database: DatabaseConfig
    telegram: TelegramConfig
    storage: StorageConfig
    logging: LoggingConfig
    drivers: DriversConfig


@lru_cache(maxsize=1)
def get_config() -> Config:
    with open("config.yaml", "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return Config(**data)