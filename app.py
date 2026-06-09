from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/price/<coin>')
def price(coin):
    params = {
        'ids': coin,
        'vs_currencies': 'usd'
    }
    r = requests.get(COINGECKO_URL, params=params).json()
    return jsonify(r)

@app.route('/api/price')
def price_query():
    coin = request.args.get('coin', 'bitcoin')
    params = {'ids': coin, 'vs_currencies': 'usd'}
    r = requests.get(COINGECKO_URL, params=params).json()
    return jsonify(r)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)