from utils.api_client import fetch_crypto_data

def test_api():

    data = fetch_crypto_data(["bitcoin"])

    assert len(data) > 0
    assert "coin" in data[0]