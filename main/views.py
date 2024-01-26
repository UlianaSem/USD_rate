from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import USDRate
from main.serializers import USDRateSerializer
from main.throttlings import CustomRateThrottle
from main.utils import get_exchange_rate


class CurrentUSDRate(APIView):
    throttle_classes = [CustomRateThrottle]

    def get(self, request, format=None):
        current_rate = get_exchange_rate()
        rates = USDRate.objects.all()[:10]

        if current_rate is None:
            return Response(
                data={"current_rate": "Ошибка запроса к Apilayer",
                      "last_rates": USDRateSerializer(rates, many=True).data},
                status=status.HTTP_200_OK)

        return Response(data={"current_rate": USDRateSerializer(current_rate).data,
                              "last_rates": USDRateSerializer(rates, many=True).data},
                        status=status.HTTP_200_OK)
