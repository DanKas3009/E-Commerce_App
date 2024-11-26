from django.db import models

# Create your models here.

class inventory(models.Model):
    inventoryID = models.AutoField(primary_key=True)
    ProductID = models.ForeignKey('Product', on_delete=models.CASCADE)
    QuantityInStock = models.IntegerField()
    ReorderLevel = models.IntegerField()
    LastRestockDate = models.DateField()
    Location = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.inventoryID