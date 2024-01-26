from rest_framework.throttling import AnonRateThrottle


class CustomRateThrottle(AnonRateThrottle):

    def parse_rate(self, rate):
        """Увеличение периода в 10 раз (с 1 до 10 секунд)"""
        num, duration = super().parse_rate(rate)

        return num, 10 * duration
