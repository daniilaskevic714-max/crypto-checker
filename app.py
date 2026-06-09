from flask import Flask, jsonify, request, render_template
import requests
import logging
from functools import lru_cache

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

@lru_cache(maxsize=256)
def fetch_price(coin: str):
    try:
        params = {'ids': coin, 'vs_currencies': 'usd'}
        r = requests.get(COINGECKO_URL, params=params, timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        logging.error(f"Price fetch error: {e}")
        return {"error": "failed to fetch price"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/price/<coin>')
def price(coin):
    return jsonify(fetch_price(coin.lower()))

@app.route('/api/price')
def price_query():
    coin = request.args.get('coin', 'bitcoin').lower()
    return jsonify(fetch_price(coin))

@app.route('/api/health')
def health():
    return jsonify({"status": "ok", "service": "crypto-checker"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)