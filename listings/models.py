from django.db import models


class Banner(models.Model):
    name= models.CharField(max_length=100, null=True)
    image= models.ImageField(upload_to='bannerimg')

    def  __str__(self):
        return self.name




class Product(models.Model):
    name=models.CharField(max_length=100, null=True)
    description= models.TextField(null=True)
    price= models.IntegerField(null=True)
    image= models.ImageField(upload_to='photos/%Y/%m/%d', null=True)
    is_publish=models.BooleanField(default=True)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
