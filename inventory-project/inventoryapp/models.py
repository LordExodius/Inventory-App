from django.db import models

# Create your models here.
class Item(models.Model):
    itemName = models.TextField("item name")
    itemDesc = models.TextField("item description")
    numItems = models.IntegerField("item quantity", default=0)

    def __str__(self) -> str:
        return (self.itemName)