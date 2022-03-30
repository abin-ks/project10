from django.db import models

# Create your models here.

class Admin_register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200,default="")
    username = models.CharField(max_length=100)
    joining_date= models.DateTimeField(null=True,blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50) 
    designation = models.CharField(max_length=100,default="")
    
    
class categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_logo = models.ImageField(default = "default.png", upload_to="images")
    sub_category1 = models.CharField(max_length=255)
    sub_category2 =  models.CharField(max_length=255)
    sub_category3 = models.EmailField(max_length=255)
    sub_category4 = models.CharField(max_length=255)
    sub_category5 = models.CharField(max_length=255)
    
    

class items(models.Model):
    modelname = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255)
    gib = models.FileField( upload_to="images/",null=True,blank=True)
    price = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    modeltype = models.CharField(max_length=255)
    cat_id =models.ForeignKey(categories, on_delete=models.DO_NOTHING, null=True,blank=True)
    fbx = models.ImageField(default="default.png", upload_to="images")


class payment(models.Model):
    modelname = models.ForeignKey(items,on_delete=models.DO_NOTHING , related_name='pay_model',null=True,blank=True)
    price = models.ForeignKey(items , on_delete=models.DO_NOTHING , related_name='pay_price',null=True,blank=True)
    clientname = models.CharField(max_length=225 ,null=True)
    date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True) 