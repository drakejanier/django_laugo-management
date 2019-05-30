from django.db import models

# Create your models here.

class laugoInventory(models.Model):
    
    itmName = models.CharField(max_length=100, blank=False) 

    ItemType = (
        ('MEDICINE','MEDICINE'),
        ('FOOD','FOOD'),
        ('OTHERS','OTHERS'),
    )
    itmType = models.CharField(max_length=20, choices=ItemType, default="MEDICINE") 

    itmQty = models.IntegerField(default=0)
    itmUnit = models.CharField(max_length=10, default="unit(s)")

    StatusOpt = (
        ('AVAILABLE','AVAILABLE'),
        ('UNAVAILABLE','OUT OF STOCK'),
        ('RESTOCKING','RESTOCKING'),
    )

    itmStatus = models.CharField(max_length=20, choices=StatusOpt, default="AVAILABLE")
    supplierID = models.IntegerField(default=0)

    class Meta: 
        abstract = True #skip this in migrations

    def __str__(self): #django to represent in django admin
        return 'Item : {0} {1}'.format(self.itmName, self.itmUnit)

class Item(laugoInventory): #inherit/pass to inventory
    pass
