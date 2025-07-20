from django.db import models
from users.models import Users  # Import your Users model


class Order(models.Model):
    user = models.CharField(max_length=100, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    # Pending, Shipped, Delivered etc.
    status = models.CharField(max_length=50, default='Pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    

    def str(self):
        return f"Order {self.id} by {self.user}"
