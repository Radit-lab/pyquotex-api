"""
Basic usage example for PyQuotex API

Modified version of PyQuotex by Cleiton Leonel Creton
Original: https://github.com/cleitonleonel/pyquotex
License: GNU GPL v3
"""

import asyncio
from pyquotex.stable_api import Quotex


async def main():
    # Initialize client
    client = Quotex(
        email="your_email@example.com",
        password="your_password",
        lang="en"
    )
    
    # Connect to Quotex
    print("Connecting to Quotex...")
    ok, reason = await client.connect()
    
    if not ok:
        print(f"Connection failed: {reason}")
        return
    
    print("Connected successfully!")
    
    # Get account balance
    balance = await client.get_balance()
    print(f"Account balance: ${balance}")
    
    # Get candles for EURUSD
    asset = "EURUSD_otc"
    period = 60  # 1 minute
    offset = 3600  # Last hour
    
    print(f"\nFetching candles for {asset}...")
    candles = await client.get_candles(asset, None, offset, period)
    
    print(f"Received {len(candles)} candles")
    print(f"Latest candle: {candles[-1]}")
    
    # Close connection
    await client.close()
    print("\nConnection closed")


if __name__ == "__main__":
    asyncio.run(main())
