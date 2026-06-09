#!/bin/bash

DOMAIN=example.com
EMAIL=admin@example.com

certbot certonly --webroot \
  -w ./certbot-www \
  -d $DOMAIN \
  --email $EMAIL \
  --agree-tos \
  --no-eff-email

docker compose -f docker-compose.prod.yml restart nginx