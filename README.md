# Crypto Checker 🚀

Полноценный production-level крипто-сервис на Python.

## 📌 Описание
Crypto Checker — это многофункциональный сервис для отслеживания криптовалют, включающий:

- 🤖 Telegram-бот для уведомлений
- 🌐 Web API (Flask)
- 📊 REST API для курсов криптовалют
- 🔔 Система подписок на цену
- 🐳 Docker инфраструктура
- 🔐 HTTPS (Nginx + Let's Encrypt)
- ⚡ Redis + PostgreSQL (готово к масштабированию)

---

## 🏗 Архитектура проекта

```
Internet
   ↓
Nginx (HTTPS / SSL termination)
   ↓
Flask App (API + Web)
   ↓
CoinGecko API
   ↓
Redis / PostgreSQL (future scaling)
```

---

## 🚀 Быстрый старт

### 1. Клонирование
```bash
git clone <repo>
cd crypto-checker
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Запуск (dev)
```bash
python run.py
```

---

## 🐳 Production запуск (HTTPS + Nginx + Docker)

### 🔧 Сборка
```bash
docker compose -f docker-compose.prod.yml up -d --build
```

### 🔐 Получение SSL сертификата
```bash
bash init-letsencrypt.sh
```

### 🌍 Доступ
```
https://your-domain.com
```

---

## 📡 API endpoints

### Получить цену
```
GET /api/price/bitcoin
```

или
```
GET /api/price?coin=bitcoin
```

### Пример ответа
```json
{
  "bitcoin": {
    "usd": 105000
  }
}
```

---

## 🤖 Telegram бот команды

- `/price bitcoin` — цена монеты
- `/subscribe bitcoin 100000` — подписка на цену
- `/subscriptions` — список подписок
- `/unsubscribe bitcoin` — удалить подписку

---

## 🐳 Docker инфраструктура

Включает:
- Flask app
- Nginx reverse proxy
- Certbot (Let's Encrypt SSL)
- Redis (кэш)
- PostgreSQL (данные)

---

## 🔐 HTTPS (Production)

Используется:
- Nginx reverse proxy
- Let's Encrypt SSL certificates
- Automatic HTTP → HTTPS redirect

---

## ⚙️ Конфигурация

Создай `.env`:
```
BOT_TOKEN=your_token_here
DATABASE_URL=sqlite:///crypto.db
```

---

## 📁 Структура проекта
```
app.py
run.py
subscriptions.py
templates/
nginx/
docker-compose.prod.yml
init-letsencrypt.sh
```

---

## 🛣 Roadmap

- [ ] WebSocket live цены
- [ ] React frontend
- [ ] User accounts
- [ ] Payment system
- [ ] AI trading signals
- [ ] Kubernetes deployment

---

## 🛡 License
Apache 2.0 — свободное использование с обязательным сохранением авторства.

---

## 👤 Author
Daniil (GitHub: daniilaskevic714-max)
