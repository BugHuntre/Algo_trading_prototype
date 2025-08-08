from config import SYMBOLS
from Utils.fetch_data import fetch_data
from Utils.indicators import calculate_rsi, calculate_moving_averages
from strategies.rsi_ma_strategy import generate_signals
from sheets.google_sheets import log_to_google_sheets
from models.predictor import train_model
from Utils.telegram_alert import send_telegram_message
import pandas as pd

if __name__ == "__main__":
    for symbol in SYMBOLS:
        try:
            # Step 1: Fetch and prepare data
            df = fetch_data(symbol)
            df = calculate_rsi(df)
            df = calculate_moving_averages(df)

            # Step 2: Generate signals
            trades = generate_signals(df)

            # Step 3: Log to Google Sheets
            log_to_google_sheets(trades)

            # Step 4: Send alerts for each trade
            for t in trades:
                try:
                    date_val = pd.to_datetime(t[1]).strftime('%Y-%m-%d')  # Ensures formatting
                    price_val = float(t[2]) if not isinstance(t[2], float) else t[2]
                    send_telegram_message(
                        f"📈 Signal: {t[0]} | {symbol} | Date: {date_val} | Price: ₹{price_val:.2f}"
                    )
                except Exception as msg_err:
                    send_telegram_message(f"⚠️ Error formatting trade alert for {symbol}: {msg_err}")

            # Step 5: Train model and send accuracy
            model, acc = train_model(df)
            send_telegram_message(f"🤖 {symbol} Model Accuracy: {acc:.2f}")
            print(f"{symbol} Model Accuracy: {acc:.2f}")

        except Exception as e:
            # Convert exception to string properly
            error_msg = f"❌ Error processing {symbol}: {str(e)}"
            print(error_msg)
            send_telegram_message(error_msg)
