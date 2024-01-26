import requests
from django.conf import settings

from main.models import USDRate

URL = "https://api.apilayer.com/exchangerates_data/latest"
PARAMS = {
  'base': 'RUB'
}
HEADERS = {
  "apikey": settings.EXCHANGE_RATE_API_KEY
}


def get_exchange_rate(currency='USD'):
    """
    Возвращает данные о курсе
    :param currency: валюта
    :return: USDRate или None в случае ошибки запроса
    """
    currency = currency.upper()

    response = requests.request("GET", URL, headers=HEADERS, params=PARAMS)
    status_code = response.status_code

    if status_code == 200:
        result = response.json()

        if result['rates'].get(currency) is not None:
            rate = USDRate.objects.create(rate=result['rates'][currency])

            return rate

    result = None

    return result
