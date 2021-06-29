import requests


def get_btc_eth():

    url = 'https://yobit.net/api/3/ticker/btc_usd-eth_usd'
    r = requests.get(url).json()
    btc_price = int(r['btc_usd']['last'])
    eth_price = int(r['eth_usd']['last'])
    return f'BTC: {btc_price} usd\nETH: {eth_price} usd'
