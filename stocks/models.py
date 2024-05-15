from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol

class Watchlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stocks = models.ManyToManyField(Stock)

    def __str__(self):
        return f"Watchlist for {self.user.username}"
