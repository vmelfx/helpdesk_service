from os import getenv

# Exchange rates service (Alpha Vantage)
ALPHA_VANTAGE_API_KEY = getenv("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_BASE_URL = getenv("ALPHA_VANTAGE_BASE_URL", default="https://www.alphavantage.co")
