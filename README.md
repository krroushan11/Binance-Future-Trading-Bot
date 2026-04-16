# Binance-Future-Trading-Bot
#  Binance Futures Testnet Trading Bot

A command-line based trading bot built in Python that allows users to place **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**.

This project demonstrates clean architecture, API integration, logging, validation, and error handling — designed as part of a Python Developer assignment.

---

##  Features

*  Place **Market Orders**
*  Place **Limit Orders**
*  Supports **BUY** and **SELL**
*  CLI-based input (argparse)
*  Structured project architecture
*  Logging of API requests & responses
*  Error handling (invalid inputs, API failures)

---

##  Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API client wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│   ├── cli.py             # CLI entry point
│
├── .env                   # API keys (not committed)
├── bot.log                # Log file
├── requirements.txt
├── README.md
```

---

##  Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```
API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_api_secret
```

---

## ▶ How to Run

Always run from the root directory using module mode:

### 🔹 Market Order

```
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### 🔹 Limit Order

```
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 30000
```

---

##  Sample Output

```
Order Successful!
Order ID    : 13039061372
Status      : NEW
Executed Qty: 0.0000
Avg Price   : 0.00
```

---

##  Logging

All activity is logged in `bot.log`, including:

* API Requests
* API Responses
* Errors (invalid input, API issues, etc.)

Example log entry:

```
INFO  | REQUEST: BTCUSDT BUY LIMIT qty=0.01 price=30000
INFO  | RESPONSE: {orderId: ..., status: NEW}
ERROR | APIError(code=-2015): Invalid API-key
```

---

##  Error Handling

The application gracefully handles:

* Invalid CLI inputs
* Missing required parameters (e.g., price for LIMIT)
* Binance API errors
* Network issues

---

##  Assumptions

* Binance **Futures Testnet (USDT-M)** is used
* Tested primarily with `BTCUSDT`
* CLI input via `argparse`
* No UI — command-line only

---

##  Requirements

All dependencies are listed in:

```
requir
```
