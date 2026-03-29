import requests
import time


def fetch_crypto_data(coins):
    all_data = []
    for coin in coins:
        url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days=1"
        
        for attempt in range(3):
            response = requests.get(url)
            if response.status_code == 200:
                break
            time.sleep(2)
        
        if response.status_code == 200:
            data = response.json()
            
            prices = data["prices"]  # [timestamp, price]
            
            for record in prices:
                all_data.append({
                    "coin": coin,
                    "timestamp": record[0],
                    "price": record[1]
                })
        else:
            print(f"Failed for {coin}")

    return all_data


def fetch_crypto_current_data(coins):
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