from django.db import models

# Create your models here.
class coffee(models.Model):
    name=models.CharField(max_length=1050)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.CharField(max_length=60000)
    class Meta:
        db_table="coffee"

