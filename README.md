# Reminder Bot

## Описание:

Проект включает следующие сервисы:
- **api** - FastAPI приложение (порт 8000)
- **redis** - Redis для Celery (порт 6379)
- **celery_worker** - Celery worker для фоновых задач
- **celery_beat** - Celery beat для периодических задач
- **telegram_bot** - Telegram бот на Telethon

## Переменные окружения:

Создайте файл `.env` со следующими переменными:

```env
# API Keys
OPENAI_API_KEY=your_openai_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# Telegram API (для Telethon)
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_PHONE=+79991234567

# Redis (для Docker используйте redis://redis:6379/0)
REDIS_URL=redis://localhost:6379/0

# Database
DATABASE_URL=sqlite:///./aibot.db
```

## Получение Telegram API credentials:

1. Перейдите на https://my.telegram.org/apps
2. Войдите с вашим номером телефона
3. Создайте новое приложение
4. Скопируйте `api_id` и `api_hash` в `.env` файл


## Telegram-бот на Telethon. Реализовано:
Основной функционал:
# Инициализация клиента — создание TelegramClient с настройками из конфига
# Авторизация — поддержка:
    # Автоматической авторизации (если сессия сохранена)
    # Авторизации по коду из SMS
    # Двухфакторной аутентификации (если включена)
Обработчики команд:
/start — приветствие
/help — список команд
/info — информация о боте

# Обработчик сообщений — базовая обработка всех входящих сообщений

Функции запуска бота:
start_bot() — асинхронный запуск
run_bot() — основной цикл работы
start_bot_sync() — синхронная обертка для запуска

Получите API credentials на https://my.telegram.org/apps
Добавьте в .env:
   TELEGRAM_API_ID=ваш_api_id   TELEGRAM_API_HASH=ваш_api_hash   TELEGRAM_PHONE=+79991234567

## Запуск проекта:

# Создайте .env файл с необходимыми переменными
# Затем запустите:docker-compose up -d# Просмотр логов:docker-compose logs -f
# Остановка:docker-compose down
