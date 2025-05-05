from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_category = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    supplier_name = models.CharField(max_length=255)
    supplier_email = models.EmailField()
    supplier_phone = models.CharField(max_length=20)
    order_status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ])
    notes = models.TextField(blank=True)
   

    def __str__(self):
        return self.item_name

class WarehouseMovement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.product_name} - {self.quantity}"


class BarcodeData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null =True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,  null=True, blank=True, related_name='barcodes')  # Add ForeignKey
    supplier_name = models.CharField(max_length=255)
    supplier_email = models.EmailField()
    item_id = models.CharField(max_length=100)
    item_name = models.CharField(max_length=255)
    barcode_number = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name
