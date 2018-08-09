from django.db import models

class Product(models.Model):
    title = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return  (self.title)