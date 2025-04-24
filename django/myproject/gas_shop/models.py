from django.db import models
from django.contrib.auth.models import User

class Attendant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.full_name

class GasCylinderSale(models.Model):
    attendant = models.ForeignKey(Attendant, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    cylinder_size = models.CharField(max_length=50)  # e.g., "6kg", "13kg"
    quantity_sold = models.PositiveIntegerField()
    price_per_cylinder = models.DecimalField(max_digits=10, decimal_places=2)

    def total_sales(self):
        return self.quantity_sold * self.price_per_cylinder

    def __str__(self):
        return f"{self.attendant} - {self.cylinder_size} x {self.quantity_sold} on {self.date}"
