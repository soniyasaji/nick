from django.db import models
from newspaper.models import News_Type
from django.contrib.auth.models import User
class Cart(models.Model):
    type=models.ForeignKey(News_Type,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateField(auto_now_add=True)

    def subtotal(self):
        return self.quantity*self.type.price

class Order(models.Model):
    type=models.ForeignKey(News_Type,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    noofitems=models.IntegerField()
    address=models.TextField()
    phone=models.CharField(max_length=200)
    order_status=models.CharField(max_length=20,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")
    date_added=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

    def subtotal(self):
        return self.noofitems*self.type.price

class Account(models.Model):
    acctnumber = models.IntegerField()
    accttype = models.CharField(max_length=200)
    balance = models.IntegerField()
    def __str__(self):
        return '%s'%(self.acctnumber)
        #return str(self.acctnumber)








