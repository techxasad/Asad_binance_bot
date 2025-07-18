from time import time
from binance.client import Client
from binance.enums import *
import logging
import time
import os
from binance.exceptions import BinanceAPIException
log_file = os.path.join(os.getcwd(), 'bot.log')  # 👈 Safe location

logging.basicConfig(filename=log_file, level=logging.INFO)

class BasicBot:
    def __init__(self,api_key,api_secret,testnet=True):
        self.client = Client(api_key,api_secret,testnet=testnet)
        self.client.TIMEOUT = 20
        self.client._timestamp_offset = self.client.get_server_time()['serverTime'] - int(time.time() * 1000)

        if testnet:
            self.client.API_URL='https://testnet.binance.vision'

    def get_account_info(self):
        try:
            account = self.client.get_account()
            logging.info(f"Account info: {account}")
            print("Connected to Binance vision API")
        except Exception as e:
            logging.error(f"Error connecting to Binance vision API: {e}")
            print(f"Credentials check failed: {e}")

    def place_market_order(self,symbol,side,quantity):
        try:
            order = self.client.create_test_order(
                symbol=symbol.upper(),
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market test order simulated: {order}")
            return {"message": "Test order sent successfully"}
        except Exception as e:
            logging.error(f"Market test order failed: {e}")
            return {"error": str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.create_test_order(
                symbol=symbol.upper(),
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=str(price)  # API requires string sometimes
            )
            logging.info(f"Limit test order simulated: {order}")
            return {"message": "✅ Limit order accepted by Binance (test simulated)"}
        
        except BinanceAPIException as e:
            logging.error(f"Binance API Error: {e}")
            # Friendly user message for common error codes
            if e.code == -1013:
                return {"error": "❌ Your order price is too far from the market price. Please try a more realistic price."}
            elif e.code == -2019:
                return {"error": "❌ Not enough balance to place the order."}
            else:
                return {"error": f"❌ Binance API Error: {e.message}"}

        except Exception as e:
            logging.error(f"Unexpected error in limit order: {e}")
            return {"error": "❌ Unexpected error. Please try again later."}
