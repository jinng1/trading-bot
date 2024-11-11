from data_pipeline import retrieve_data

# Example usage
symbol = "BTCUSDT"  # Example: you can replace this with other symbols
interval = "1h"  # Example interval (1 hour)
start_time = "1 Jan, 2022"  # Start date for historical data
filename = f"data_pipeline/data/{symbol}_historical_data_{interval}.csv"  # Output file name

# Download data
df = retrieve_data.download_historical_data(symbol, interval, start_time, filename)

