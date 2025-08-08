import yfinance as yf
import pandas as pd
import os
from config import USE_API

def fetch_data(symbol, period="6mo", interval="1d"):
    file_path = f"data/{symbol.replace('.NS','')}.csv"

    if USE_API:
        try:
            df = yf.download(symbol, period=period, interval=interval, auto_adjust=True)
            if df is None or df.empty:
                raise ValueError(f"No data returned for {symbol}")
            df.to_csv(file_path)
        except Exception as e:
            raise ValueError(f"❌ Error fetching {symbol}: {str(e)}")
    else:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        df = pd.read_csv(file_path, index_col="Date", parse_dates=True)

    df.dropna(inplace=True)
    return df
