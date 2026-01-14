"""Telegram бот на Telethon"""
import asyncio
import logging
from typing import Optional

from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError

from app.config import settings

logger = logging.getLogger(__name__)

# Создаем клиент Telethon
client = TelegramClient(
    "aibot_session",  # имя файла сессии; он будет создан рядом с точкой запуска
    api_id=settings.telegram_api_id,
    api_hash=settings.telegram_api_hash,
)



async def start_bot():
    """Запуск бота"""
    await client.start(phone=settings.telegram_phone)
    
    if not await client.is_user_authorized():
        logger.info("Отправка кода авторизации...")
        await client.send_code_request(settings.telegram_phone)
        
        code = input('Введите код из Telegram: ')
        try:
            await client.sign_in(settings.telegram_phone, code)
        except SessionPasswordNeededError:
            password = input('Введите пароль двухфакторной аутентификации: ')
            await client.sign_in(password=password)
    
    logger.info("Бот успешно запущен!")
    me = await client.get_me()
    logger.info(f"Авторизован как: {me.first_name} (@{me.username})")


@client.on(events.NewMessage(pattern='(?i)/start'))
async def handle_start(event: events.NewMessage.Event):
    """Обработчик команды /start"""
    await event.respond('Привет! Я AI бот. Используй /help для списка команд.')


@client.on(events.NewMessage(pattern='(?i)/help'))
async def handle_help(event: events.NewMessage.Event):
    """Обработчик команды /help"""
    help_text = """
Доступные команды:
/start - Начать работу с ботом
/help - Показать это сообщение
/info - Информация о боте
"""
    await event.respond(help_text)


@client.on(events.NewMessage(pattern='(?i)/info'))
async def handle_info(event: events.NewMessage.Event):
    """Обработчик команды /info"""
    me = await client.get_me()
    info_text = f"""
Информация о боте:
Имя: {me.first_name}
Фамилия: {me.last_name or 'Не указана'}
Username: @{me.username or 'Не указан'}
ID: {me.id}
"""
    await event.respond(info_text)


@client.on(events.NewMessage)
async def handle_message(event: events.NewMessage.Event):
    """Обработчик всех сообщений"""
    # Пропускаем команды и служебные сообщения
    if event.message.text and event.message.text.startswith('/'):
        return
    
    # Пропускаем сообщения от самого себя
    if event.message.out:
        return
    
    # Здесь можно добавить логику обработки обычных сообщений
    # Например, отправка в AI для генерации ответа
    logger.info(f"Получено сообщение от {event.sender_id}: {event.message.text}")


async def run_bot():
    """Запуск бота в бесконечном цикле"""
    try:
        await start_bot()
        await client.run_until_disconnected()
    except Exception as e:
        logger.error(f"Ошибка при работе бота: {e}", exc_info=True)
    finally:
        await client.disconnect()


def start_bot_sync():
    """Синхронная функция для запуска бота"""
    asyncio.run(run_bot())


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    start_bot_sync()
