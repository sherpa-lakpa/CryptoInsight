def test_dedup():

    sample = [
        {"coin": "btc", "price": 10},
        {"coin": "btc", "price": 10}
    ]

    unique = {tuple(d.items()) for d in sample}

    assert len(unique) == 1