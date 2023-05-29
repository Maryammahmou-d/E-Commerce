from django.db import models
# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    def __str__(self) :
        return self.name
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
    
class CustomerModel(models.Model):
    Username = models.CharField(max_length=50, null=True)
    Password = models.CharField(max_length=50, null=True)
    Email = models.CharField(max_length=100, null= True)
    Products = models.ManyToManyField(Product, related_name='Products')

    def __str__(self) :
        return str(self.Username)

    

class Order (models.Model):
    customer=models.ForeignKey(CustomerModel,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self) :
        return str(self.id)
    
          
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(CustomerModel,on_delete=models.SET,blank=True,null=True)
   
# a model that has the items and the user who owns them
class CartItem(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.customer} - {self.product}"
