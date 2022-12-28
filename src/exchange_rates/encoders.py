"""Creating custom JSONEncoder to be able to return decimal instead of str"""

import json
from decimal import Decimal

from django.http import JsonResponse


class ForDecimalJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        else:
            return super().default(o)


class ForDecimalJsonResponse(JsonResponse):
    def __init__(
        self,
        data,
        **kwargs,
    ):
        JsonResponse.__init__(self, data, encoder=ForDecimalJsonEncoder, safe=True, json_dumps_params=None, **kwargs)
