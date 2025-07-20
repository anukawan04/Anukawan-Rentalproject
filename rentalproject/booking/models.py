from django.db import models


from users.models import Users  # Import your Users model


class Booking(models.Model):
    user = models.CharField(max_length=100, blank=True, null=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    vehicle_number = models.CharField(max_length=20)
    scheduled_time = models.DateTimeField()
    service = models.CharField(max_length=100)

    def str(self):
        return f"Booking {self.id} by {self.user}"
