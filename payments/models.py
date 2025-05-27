# payments/models.py
from django.db import models

class Item(models.Model):
    CURRENCIES = (
        ('usd', 'USD'),
        ('eur', 'EUR'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='usd')

    def __str__(self):
        return f"{self.name} ({self.price} {self.currency.upper()})"

class Discount(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.percentage}%"

class Tax(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.percentage}%"

class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        total = sum([item.price for item in self.items.all()])
        if self.discount:
            total *= (1 - self.discount.percentage / 100)
        if self.tax:
            total *= (1 + self.tax.percentage / 100)
        return round(total, 2)

    def currency(self):
        # Возвращает валюту первого товара
        return self.items.first().currency if self.items.exists() else 'usd'

    def __str__(self):
        return f"Order #{self.pk}"