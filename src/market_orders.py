from bot import BasicBot
from dotenv import load_dotenv
import os

load_dotenv("api_key.env")

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

bot = BasicBot(API_KEY, API_SECRET)
bot.get_account_info()

symbol = input("Symbol: ")
side = input("Side (buy/sell): ").lower()
quantity = float(input("Quantity: "))

result = bot.place_market_order(symbol, side, quantity)
print("Order Result:", result)
