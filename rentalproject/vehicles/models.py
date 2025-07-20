from django.db import models
from users.models import Users


class Vehicles(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='vehicles')
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_model = models.CharField(max_length=50)
    # Optional: Car, Bike, etc.
    vehicle_type = models.CharField(max_length=30, blank=True, null=True)
    # Optional: Vehicle color
    color = models.CharField(max_length=30, blank=True, null=True)

    def str(self):
        return f"{self.vehicle_model} ({self.vehicle_number}) owned by {self.user.name}"
