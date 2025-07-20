from django.db import models


class Payment(models.Model):
    # order = models.OneToOneField( on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)  # e.g., Card, PayPal, COD
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50, default='Unpaid')

    def str(self):
        return self.payment_method
