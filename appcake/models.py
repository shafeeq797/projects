from django.db import models
class tbl_user(models.Model):
    first_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    photo=models.CharField(max_length=600)
    class Meta:
        db_table="tbl_user"
class tbl_cake(models.Model):
    cakename=models.CharField(max_length=50)
    quantity=models.IntegerField()
    flavour=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.CharField(max_length=600)
    class Meta:
        db_table="tbl_cake"




# Create your models here.
