from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    category = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    deactivation_date = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


