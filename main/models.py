from django.db import models


class USDRate(models.Model):
    rate = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="значение курса")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.rate

    class Meta:
        verbose_name = "курс доллара"
        verbose_name_plural = "курсы доллара"
        ordering = ('-created_at', )
