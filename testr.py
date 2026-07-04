from core.config import get_config

config = get_config()

print(config.app.name)
print(config.telegram.chat_id)