from django.db import models
from datetime import datetime

class APIdata(models.Model):
    country = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now=datetime.now())
    cases = models.CharField(max_length=100)
    deaths = models.CharField(max_length=100)
    recovered = models.CharField(max_length=100)

    def __str__(self):
        return self.country

    # destructor
    def __del__(self):
        return

    class Meta:
        verbose_name = 'API DATA'
        verbose_name_plural = 'APIS DATA'