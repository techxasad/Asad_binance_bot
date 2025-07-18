import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 👈 Move this to the top

from src.bot import BasicBot
from advanced.twap import TWAPBot
from advanced.oco import OCOBot
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
env_path = Path(__file__).resolve().parent / 'api_key.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

print("🔐 API Key Loaded:", API_KEY is not None)
print("🔐 API Secret Loaded:", API_SECRET is not None)

# Initialize the bot
bot = BasicBot(API_KEY, API_SECRET)
bot.get_account_info()

# Strategy selection
print("\n📊 Binance Trading Bot")
print("Choose strategy:")
print("1. Market Order")
print("2. Limit Order")
print("3. TWAP Strategy")


choice = input("Enter your choice (1-3): ")
result = {}

if choice == "1":
    symbol = input("Symbol (e.g., BTCUSDT): ").upper()
    side = input("Side (buy/sell): ").lower()
    quantity = float(input("Quantity: "))
    result = bot.place_market_order(symbol, side, quantity)

elif choice == "2":
    symbol = input("Symbol (e.g., BTCUSDT): ").upper()
    side = input("Side (buy/sell): ").lower()
    quantity = float(input("Quantity: "))
    try:
        ticker = bot.client.get_symbol_ticker(symbol=symbol)
        print(f"📊 Current {symbol} market price: {ticker['price']} USDT")
        price = float(input("Enter your limit price: "))
        result = bot.place_limit_order(symbol, side, quantity, price)
    except Exception as e:
        result = {"error": f"❌ Error fetching market price or placing order: {e}"}

elif choice == "3":
    twap = TWAPBot(bot)
    symbol = input("Symbol (e.g., BTCUSDT): ").upper()
    side = input("Side (buy/sell): ").lower()
    total_quantity = float(input("Total quantity: "))
    chunks = int(input("Number of chunks: "))
    interval_sec = int(input("Interval between orders (sec): "))
    twap.execute_twap(symbol, side, total_quantity, chunks, interval_sec)
    result = {"message": "✅ TWAP strategy executed."}


else:
    result = {"error": "❌ Invalid choice. Please enter a number between 1 and 4."}

# Display result
print("\n🧾 Order Result:")
print(result["message"] if "message" in result else result["error"])