import requests
from django.conf import settings
from exchange_rates.domain import (
    AlphavantageResponse,
    ExchangeRatesServiceRequest,
    ExchangeRatesServiceResponse,
)


class ExchangeRatesService:
    """This exchange rates service works with 3-rd party  AlphaVantage interface"""

    def __init__(self, request: ExchangeRatesServiceRequest) -> None:
        self._request: ExchangeRatesServiceRequest = request

    def _build_url(self) -> str:
        return (
            f"{settings.ALPHA_VANTAGE_BASE_URL}/query?"
            f"function=CURRENCY_EXCHANGE_RATE&from_currency={self._request.from_currency}"
            f"&to_currency={self._request.to_currency}&apikey={settings.ALPHA_VANTAGE_API_KEY}"
        )

    def convert(self) -> ExchangeRatesServiceResponse:
        url = self._build_url()
        response: requests.Response = requests.get(url)
        alphavantage_response = AlphavantageResponse(**response.json())
        return ExchangeRatesServiceResponse(rate=alphavantage_response.results.rate)
