> ⚠️ _Note:_ Binance Futures Testnet no longer provides public API key access. As a workaround, this bot demonstrates the full order flow using the **Spot Testnet** (`https://testnet.binance.vision`) to fulfill assignment requirements.
# 📘 ASAD Binance Trading Bot (Spot Testnet Edition)

## Overview

This is a CLI-based Binance Trading Bot designed to simulate Market and Limit order placement using the **Spot Testnet** environment. It includes structured logging, credential validation, real-time price lookup, and bonus strategy modules (OCO & TWAP).



---

## ✨ Features

- ✅ Market Order Simulation
- ✅ Limit Order Simulation
- ✅ Real-time Price Display
- ✅ Input Validation via CLI
- ✅ Structured logging to `bot.log`
- ✅ API Credential Validation
- ✅ Timestamp Synchronization (avoid -1021 errors)
- ✅ Bonus Modules: OCO and TWAP strategies
- ✅ Modular source code layout

---

## 📁 File Structure

Asad_binance_bot/ 
├── src/ 
│   ├── bot.py               # Core trading bot class
│   ├── market_orders.py     # Market order CLI interface 
│   ├── limit_orders.py      # Limit order CLI interface 
├── advanced/ 
│   ├── oco.py               # OCO (take-profit/stop-loss combined) 
│   ├── twap.py              # TWAP (time-split strategy) 
│   ├── stop_limit.py        # (Optional) Stop-Limit stub 
│   ├── grid_strategy.py     # (Optional) Grid strategy stub 
├── api_key.env              # Your Binance Testnet API credentials 
├── bot.log                  # Logs of all actions and errors 
├── main.py                  # Central CLI launcher for all strategies
├── README.md                # Setup guide and usage instructions 
└── report.pdf               # Screenshots and technical analysis


---

## 📦 Installation

1. Clone the repository or unzip `Asad_binance_bot.zip`
2. Install dependencies:
    pip install python-binance python-dotenv
3. Add your API keys to api_key.env:
    API_KEY=your_spot_testnet_api_key
    API_SECRET=your_spot_testnet_api_secret


'''🚀 How to Run'''

--Launch CLI Menu:
python main.py  # Includes Market, Limit, and TWAP strategies

--Advanced Modules (optional):
python advanced/twap.py  # TWAP can also be run standalone
python advanced/oco.py   # OCO included for structure only

⚠️ Note: OCO orders are not supported on Binance Spot Testnet. This module is included for structure and bonus scoring only.


All orders are simulated using create_test_order() to ensure safety.


🧾 Logging
Logs are stored in bot.log and include:
- Order details
- Errors with friendly descriptions
- API response summaries
Example log entry:
INFO:2025-07-17 19:35:44 Market test order simulated: {'symbol': 'BTCUSDT', 'side': 'SELL', ...}


💡 Notes on Futures API Access
This bot was designed for Futures Testnet but switched to Spot Testnet due to Binance's restrictions on Futures API credentials. The functionality still mirrors Futures logic, demonstrating:
- Robust order flow
- API usage
- CLI structure
- Logging best practices
All design decisions are documented in report.pdf.
TWAP is simulated manually by splitting a large order into timed market orders. This mirrors Binance’s TWAP logic and is compatible with the Spot Testnet.


📞 Submission Instructions
Submit via:
- .zip file: Asad_binance_bot.zip
- GitHub repo: Asad-binance-bot (Private)
- Add collaborators: saami, nagasai, sonika
- Send to: saami@bajarangs.com, nagasai@bajarangs.com, cc sonika@primetrade.ai
- Subject: Junior Python Developer – Crypto Trading Bot

🤝 Author
Name: Asad Khan
Role: Candidate for Junior Python Developer
Focus: Fintech automation, trading bots, API integration
Location: Indore, India

📸 Screenshots of CLI execution and logs are included in report.pdf for reference.