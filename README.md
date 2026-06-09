# Crypto Checker 🚀 (Big Tech SaaS Edition)

Полноценная cloud-native SaaS платформа для отслеживания криптовалют с уровнем архитектуры как у fintech и биржевых систем.

---

## 📌 Описание

Crypto Checker — это распределённый крипто-сервис с:

- 🤖 Telegram bot (уведомления и подписки)
- 🌐 Flask API + Web interface
- 🔐 JWT authentication (SaaS users)
- 🧠 Rate limiting + anti-bot protection
- 🐳 Docker production stack
- ☸️ Kubernetes deployment ready
- 🌍 Cloudflare WAF integration
- 🔐 HTTPS (Nginx + Let's Encrypt)
- ⚡ Redis caching layer
- 🗄 PostgreSQL ready architecture

---

## 🏗 BIG TECH ARCHITECTURE

```
User
  ↓
Cloudflare (WAF + DDoS + Bot Protection)
  ↓
Nginx Ingress (TLS + Reverse Proxy)
  ↓
Kubernetes Service
  ↓
Flask App (3+ replicas)
  ↓
Redis Cache / PostgreSQL DB
  ↓
CoinGecko API
```

---

## 🔐 Security Stack (Enterprise Level)

- 🛡 Cloudflare WAF rules (bot filtering, geo blocking, API protection)
- 🚫 Fail2Ban intrusion prevention
- ⚡ Nginx rate limiting
- 🔐 JWT authentication layer
- 🧱 Kubernetes network isolation
- 🌍 Origin IP protection (no direct server access)

---

## 🚀 Quick Start (Dev)

```bash
git clone <repo>
cd crypto-checker
pip install -r requirements.txt
python run.py
```

---

## 🐳 Production Deployment (Docker + HTTPS)

```bash
docker compose -f docker-compose.prod.yml up -d --build
bash init-letsencrypt.sh
```

Access:
```
https://your-domain.com
```

---

## ☸️ Kubernetes Deployment (Big Tech Mode)

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

---

## 📡 API Endpoints

### Public
```
GET /api/price/bitcoin
GET /api/price?coin=bitcoin
```

### Auth Required (JWT)
```
Authorization: Bearer <token>
```

---

## 🤖 Telegram Bot Commands

- /price bitcoin
- /subscribe bitcoin 100000
- /unsubscribe bitcoin
- /subscriptions

---

## 🔐 Authentication (SaaS Layer)

- JWT tokens (HS256)
- User registration & login
- Protected API routes
- Token expiration (24h)

---

## ☁️ Cloudflare Integration

- WAF (Web Application Firewall)
- Bot Fight Mode
- Rate limiting at edge
- DDoS protection (L3-L7)
- Origin IP hiding

---

## ⚡ Performance Layer

- Redis caching (price requests)
- Horizontal scaling (Kubernetes replicas)
- Load balancing via Ingress

---

## 📁 Project Structure

```
app.py
run.py
auth.py
subscriptions.py
nginx/
cloudflare/
k8s/
docker-compose.prod.yml
init-letsencrypt.sh
```

---

## 🛣 Roadmap (SaaS Evolution)

- [x] JWT Authentication
- [x] Kubernetes deployment
- [x] Cloudflare WAF integration
- [ ] WebSocket real-time pricing
- [ ] Stripe payments (monetization)
- [ ] React frontend dashboard
- [ ] AI trading signals
- [ ] Multi-region deployment

---

## 🧠 Observability (Future)

- Prometheus metrics
- Grafana dashboards
- Centralized logging (Loki)
- Alerting system

---

## 🛡 License
Apache 2.0 — with attribution requirement.

---

## 👤 Author
Daniil (GitHub: daniilaskevic714-max)
