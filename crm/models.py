from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.customer_name