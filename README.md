# Crypto Checker

Современный крипто-проект на Python с Telegram-ботом и веб-интерфейсом.

## Возможности
- Получение курсов криптовалют
- Telegram-бот
- Веб-сайт
- Подписки и уведомления
- SQLite

## Установка
```bash
git clone <repo>
cd crypto-checker
pip install -r requirements.txt
```

## Запуск
```bash
python main.py
```

## Команды
- /price bitcoin
- /subscribe bitcoin 100000
- /subscriptions
- /unsubscribe bitcoin

## Архитектура
- main.py
- subscriptions.py
- templates/

## Планы развития
- Flask
- Docker
- Графики
- Авторизация
- GitHub Actions