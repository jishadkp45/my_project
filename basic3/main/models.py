from django.db import models


# Create your models here.
class ProductModel(models.Model):
    name=models.CharField(max_length=60,unique=True,null=False,blank=False)
    price=models.IntegerField()
    description=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='product_Table'

    def __str__(self):
        return self.name




class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()