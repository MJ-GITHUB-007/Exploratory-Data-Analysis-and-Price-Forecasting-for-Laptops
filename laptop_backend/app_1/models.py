from django.db import models
from datetime import datetime

# Create your models here.
class Input_data(models.Model):
    Company = models.CharField(max_length=10)
    TypeName = models.CharField(max_length=25)
    CPU_Brand = models.CharField(max_length=25)
    CPU_Frequency = models.DecimalField(max_digits=2, decimal_places=1)
    OpSys = models.CharField(max_length=20)
    RAM = models.SmallIntegerField()
    GPU = models.CharField(max_length=6)
    Memory_SSD = models.SmallIntegerField()
    Price = models.SmallIntegerField(default=0)
    date_time = models.DateField(default=datetime.now())

    def __str__(self):
        return self.Company + '_$' + str(self.Price)
    
