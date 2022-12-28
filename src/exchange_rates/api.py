import json

from exchange_rates.domain import (
    ExchangeRatesServiceRequest,
    ExchangeRatesServiceResponse,
)
from exchange_rates.encoders import ForDecimalJsonResponse
from exchange_rates.services import ExchangeRatesService


def convert(request):
    if request.method == "POST":
        request_json = json.loads(request.body)
        from_currency = request_json["from"]
        to_currency = request_json["to"]
        exchange_rates_service = ExchangeRatesService(
            request=ExchangeRatesServiceRequest(from_currency=from_currency, to_currency=to_currency)
        )
        result: ExchangeRatesServiceResponse = exchange_rates_service.convert()
        return ForDecimalJsonResponse(result.dict())
