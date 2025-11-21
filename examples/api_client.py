"""
Example API client for PyQuotex REST API

Modified version of PyQuotex by Cleiton Leonel Creton
Original: https://github.com/cleitonleonel/pyquotex
License: GNU GPL v3
"""

import requests


def get_candles(base_url: str, asset: str, count: int = 50, period: int = 60):
    """Fetch candles from API"""
    response = requests.get(
        f"{base_url}/candles/last",
        params={
            "asset": asset,
            "count": count,
            "period": period
        }
    )
    response.raise_for_status()
    return response.json()


def main():
    # API base URL (change to your deployed URL)
    BASE_URL = "http://localhost:10000"
    
    # Check health
    health = requests.get(f"{BASE_URL}/health").json()
    print(f"API Status: {health['status']}")
    
    # Get candles
    asset = "EURUSD_otc"
    data = get_candles(BASE_URL, asset, count=100, period=60)
    
    print(f"\nAsset: {data['asset']}")
    print(f"Period: {data['period']}s")
    print(f"Candles: {data['count']}")
    
    # Show last 5 candles
    print("\nLast 5 candles:")
    for candle in data['candles'][-5:]:
        print(f"  {candle['date']} {candle['time_hm']} - "
              f"O:{candle['open']:.5f} C:{candle['close']:.5f} "
              f"[{candle['color']}]")


if __name__ == "__main__":
    main()
