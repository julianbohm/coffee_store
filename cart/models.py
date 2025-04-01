from django.db import models
from django.contrib.auth.models import User
from products.models import Coffee

# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.coffee.name} for {self.user.username}"

    def get_total_price(self):
        return self.quantity * self.coffee.price