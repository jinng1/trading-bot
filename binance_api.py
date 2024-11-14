import os
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables from .env file (if using)
load_dotenv()

# Retrieve your API keys from environment variables
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')

# Initialize the Binance client with your API keys
client = Client(api_key, api_secret, testnet=False)  # Set testnet=True if using Binance testnet
