# Cloudflare Integration (Enterprise Edge Security)

## 🌐 What Cloudflare does
Using Cloudflare (a global edge security network by Cloudflare, Inc.) adds a protection layer in front of your server:

- 🛡 DDoS mitigation (L3/L4/L7)
- 🚫 Bot filtering
- 🔐 WAF (Web Application Firewall)
- 🌍 IP masking (origin protection)
- ⚡ CDN caching

---

## 🧱 Recommended Setup

### 1. DNS Configuration
In Cloudflare dashboard:
- Add A record → your server IP
- Enable **Proxy (orange cloud ☁️ ON)**

---

## 🔐 2. Origin Protection (IMPORTANT)
Block direct access to your server IP:

Allow only Cloudflare IPs in firewall:

```bash
# Example UFW rules
ufw allow from 173.245.48.0/20 to any port 80
ufw allow from 173.245.48.0/20 to any port 443
```

(Use full official Cloudflare IP list)

---

## ⚙️ 3. Nginx Real IP Fix
So logs show real users, not Cloudflare:

```nginx
set_real_ip_from 173.245.48.0/20;
set_real_ip_from 103.21.244.0/22;
real_ip_header CF-Connecting-IP;
```

---

## 🚀 4. Recommended Cloudflare Settings

- SSL mode: **Full (strict)** 🔐
- Always Use HTTPS: ON
- HTTP/3: ON
- Bot Fight Mode: ON
- Rate Limiting: enabled

---

## 🧠 5. Optional Enterprise Features

- Workers (edge functions)
- Argo Smart Routing
- Advanced WAF rules
- Zero Trust access control

---

## 🧪 Architecture

Internet → Cloudflare Edge → Nginx → Flask App → API

---

## ⚠️ Security Rule
Never expose origin IP publicly. Always route traffic through Cloudflare.

---

## 💎 Result
With Cloudflare enabled, your system gets:
- Enterprise DDoS protection
- Bot filtering at edge
- Faster global response times
- Hidden origin server
