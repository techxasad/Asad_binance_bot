import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import time
from src.bot import BasicBot  # ✅ Now Python knows where to find src.bot

class TWAPBot:
    def __init__(self, bot):
        self.bot = bot

    def execute_twap(self, symbol, side, total_quantity, chunks, interval_sec):
        quantity_per_order = round(total_quantity / chunks, 6)
        for i in range(chunks):
            print(f"Placing chunk {i + 1}/{chunks}")
            result = self.bot.place_market_order(symbol, side, quantity_per_order)
            print("Result:", result)
            time.sleep(interval_sec)

# 🟢 CLI Execution Block
if __name__ == "__main__":
    from dotenv import load_dotenv
    import os

    load_dotenv("api_key.env")
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")

    bot = BasicBot(API_KEY, API_SECRET)
    twap_strategy = TWAPBot(bot)

    print("\n📊 TWAP Strategy Execution")
    symbol = input("Symbol (e.g., BTCUSDT): ").upper()
    side = input("Side (buy/sell): ").lower()
    total_quantity = float(input("Total quantity: "))
    chunks = int(input("Number of chunks: "))
    interval_sec = int(input("Interval between orders (sec): "))

    twap_strategy.execute_twap(symbol, side, total_quantity, chunks, interval_sec)