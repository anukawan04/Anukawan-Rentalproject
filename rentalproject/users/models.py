from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField()
    password = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)

    def str(self):
        return self.name
