from decimal import Decimal

from pydantic import BaseModel, Field


class ExchangeRatesResults(BaseModel):
    rate: Decimal = Field(alias="5. Exchange Rate")


class AlphavantageResponse(BaseModel):
    results: ExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")


class ExchangeRatesServiceRequest(BaseModel):
    from_currency: str
    to_currency: str


class ExchangeRatesServiceResponse(BaseModel):
    rate: Decimal
