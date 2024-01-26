from rest_framework.serializers import ModelSerializer

from main.models import USDRate


class USDRateSerializer(ModelSerializer):

    class Meta:
        model = USDRate
        fields = ['rate', 'created_at']
