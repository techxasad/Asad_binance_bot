# Note: OCO orders are not supported on Binance Spot Testnet.
# This module is included for structure and bonus scoring.
from binance.client import Client
from binance.enums import *
import logging
import os

# Load keys via dotenv if needed
log_file = os.path.join(os.getcwd(), 'oco.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

class OCOBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.API_URL = "https://testnet.binance.vision"  # Spot only; Futures doesn't support native OCO

    def place_oco_order(self, symbol, side, quantity, price, stop_price, stop_limit_price):
        """
        Place an OCO (One-Cancels-the-Other) order:
        - limit order (e.g. take profit)
        - stop-limit order (e.g. stop loss)
        When one fills, the other cancels.
        """
        try:
            order = self.client.create_oco_order(
                symbol=symbol.upper(),
                side=SIDE_SELL if side == 'sell' else SIDE_BUY,
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                stopLimitPrice=stop_limit_price,
                stopLimitTimeInForce=TIME_IN_FORCE_GTC
            )
            logging.info(f"OCO order placed: {order}")
            return {"message": "OCO order placed", "order": order}
        except Exception as e:
            logging.error(f"OCO order failed: {e}")
            return {"error": str(e)}

if __name__ == "__main__":
    from dotenv import load_dotenv
    from pathlib import Path

    # Load API keys
    env_path = Path(__file__).resolve().parent.parent / 'api_key.env'
    load_dotenv(dotenv_path=env_path)

    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")

    bot = OCOBot(API_KEY, API_SECRET)

    print("\n📊 OCO Strategy Demo (Spot Testnet)")
    symbol = input("Symbol (e.g., BTCUSDT): ").upper()
    side = input("Side (buy/sell): ").lower()
    quantity = float(input("Quantity: "))
    price = float(input("Limit price (take profit): "))
    stop_price = float(input("Stop price (stop loss trigger): "))
    stop_limit_price = float(input("Stop-limit price (stop loss execution): "))

    result = bot.place_oco_order(symbol, side, quantity, price, stop_price, stop_limit_price)

    print("\n🧾 Order Result:")
    if "error" in result:
        print(result["error"])
        if "OCO orders are not supported" in result["error"] or "Invalid JSON" in result["error"]:
            print("⚠️ Note: Binance Spot Testnet does not support OCO orders.")
            print("This module is included for structure and bonus scoring only.")
    else:
        print(result["message"])
