from django.db import models
class A(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField(max_length=10)
    def __str__(self):
        return self.name
class B(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField(max_length=10)
    def __str__(self):
        return self.name        

    
# Create your models here.
