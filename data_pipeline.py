import pandas as pd
from . import binance_api
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def fetch_data(symbol: str, interval: str, start_time: str, filename: str):
    # Fetch historical data (candlestick data)
    client = binance_api.client
    klines = client.get_historical_klines(symbol, interval, start_str=start_time)

    # Convert the raw data into a pandas DataFrame for easier manipulation
    df = pd.DataFrame(klines, columns=["Open Time", "Open", "High", "Low", "Close", "Volume", "Close Time", "Quote Asset Volume", "Number of Trades", "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "Ignore"])

    # Convert the "Open Time" and "Close Time" to readable date format
    df["Open Time"] = pd.to_datetime(df["Open Time"], unit='ms')
    df["Close Time"] = pd.to_datetime(df["Close Time"], unit='ms')

    # Optionally, drop columns you don't need (e.g., "Ignore")
    df.drop(columns=["Ignore"], inplace=True)

    # Save the data to a CSV file
    df.to_csv("data/" + filename, index=False)

    print(f"Data saved to {filename}")
    return df.head()  # Return the first few rows for preview
