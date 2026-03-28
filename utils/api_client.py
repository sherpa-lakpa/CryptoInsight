import requests

def fetch_crypto_data(coins):
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": ",".join(coins),
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    records = []
    for coin, value in data.items():
        records.append({
            "coin": coin,
            "price": value["usd"]
        })

    return records