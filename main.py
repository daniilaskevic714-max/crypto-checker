import requests
coin=input('Введите монету: ').lower()
url=f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
res=requests.get(url).json()
print(f'Курс {coin}:', res.get(coin,{}).get('usd','не найден'))