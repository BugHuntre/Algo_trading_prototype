# 📊 Algo-Trading System with ML & Automation

This is a Python-based mini algorithmic trading system that:
- Fetches stock data via Yahoo Finance
- Applies a combined RSI + Moving Average crossover strategy
- Logs trades & metrics to Google Sheets
- Uses a Decision Tree ML model for price direction prediction
- Sends real-time alerts to Telegram

---
## 🚀 Features

| Feature                                | Status |
|----------------------------------------|--------|
| Fetch stock data (Yahoo Finance)       | ✅      |
| RSI < 30 + 20DMA > 50DMA strategy      | ✅      |
| 6-month backtest                       | ✅      |
| Decision Tree model on RSI, MACD, Volume | ✅   |
| Prediction accuracy logged             | ✅      |
| Log trades to Google Sheets            | ✅      |
| Portfolio P&L & summary tabs           | ✅      |
| 📢 Telegram alerts for signals/errors  | ✅      |
| Modular Python code                    | ✅      |

---

## 🧠 Tech Stack

- Python, Pandas, scikit-learn
- gspread, oauth2client
- Yahoo Finance API (via yfinance)
- Telegram Bot API

---
