from django.db import models
from ..customer.models import Customer

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    OrderDate = models.DateField()
    CustomerID = models.ForeignKey( Customer , on_delete=models.CASCADE)
     
    OrderTotal = models.DecimalField(max_digits=10, decimal_places=2)
    OrderStatus = models.CharField(max_length=100)
    ShippingAddress = models.CharField(max_length=300)

    def __str__(self):
        return self.orderID

class OrderDetails(models.Model):
    orderDetailsID = models.AutoField(primary_key=True)
    Order = models.ForeignKey('Order', on_delete=models.CASCADE)
    Product = models.ForeignKey('Product', on_delete=models.CASCADE)  
    Quantity = models.PositiveIntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.orderDetailsID

class Inventory(models.Model):
    inventoryID = models.AutoField(primary_key=True)
    Product = models.OneToOneField('Product', on_delete=models.CASCADE, primary_key=True)
    QuantityInStock = models.PositiveIntegerField()
    ReorderLevel = models.PositiveIntegerField()
    LastRestockDate = models.DateField()
    Location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.inventoryID)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()  

    image = models.ImageField(upload_to='product_images/')  

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    cartID = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)  # Assuming a Customer model
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cartID)

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField() 

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"