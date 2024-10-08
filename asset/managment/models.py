from django.db import models

from django.contrib.auth.models import User

from django.conf import settings

class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField("username",max_length=100)
    password=models.CharField("password",max_length=100)
    role=models.CharField("role",max_length=100)

class Employee(models.Model):
    Employee_id = models.AutoField(primary_key=True)
    Employee_name=models.CharField("Employee_name",max_length=100)
    Designation=models.CharField("Designation",max_length=100)
    Gender=models.CharField("Gender",max_length=100)
    Address=models.CharField("Company_Name",max_length=100)
    Phone=models.CharField("Phone",max_length=100)
    Place=models.CharField("Place",max_length=100)
    Email=models.CharField("Email",max_length=100)
    logid=models.ForeignKey(login,on_delete=models.CASCADE,null=True)

# models.py


class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    Product_Name = models.CharField("Product Name", max_length=100)
    Image = models.FileField("Image", upload_to='images/')
    Description = models.CharField("Description", max_length=500)
    Specification = models.CharField("Specification", max_length=100)
    Quantity = models.IntegerField("Quantity")
    Amount = models.DecimalField("Amount", max_digits=10, decimal_places=2)

    
class Request(models.Model):
    Request_id = models.AutoField(primary_key=True)
    Employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    Product_id = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    from_date = models.DateField("from_date", null=True)
    Return_Date = models.DateField("Return_Date", null=True)
    Status = models.CharField("Status", max_length=100)
    Penalty = models.CharField("Penalty", max_length=100)
    Defect = models.CharField("Defect", max_length=100)
    Purpose = models.CharField("Purpose", max_length=100)



class Penalty(models.Model):
    penalty_id = models.AutoField(primary_key=True)
    request = models.ForeignKey('Request', on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, related_name='penalty_giver')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.CharField(max_length=255)


    def __str__(self):
        return f"Penalty {self.penalty_id} - {self.amount}"

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField("first_name", max_length=100)
    last_name = models.CharField("last_name", max_length=100)
    gender = models.CharField("gender", max_length=100)
    phone_number = models.CharField("phone_number", max_length=15, null=True, blank=True)
    pincode = models.CharField("pincode", max_length=100)
    address=models.CharField("address",max_length=100)
    state=models.CharField("state",max_length=100)
    city=models.CharField("city",max_length=100)
    date_of_birth = models.DateField("date_of_birth", null=True, blank=True)
    email = models.EmailField("email", unique=True)
    log_user_id=models.ForeignKey(login,on_delete=models.CASCADE,null=True)


# from geopy.geocoders import Nominatim

# class Location(models.Model):
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     postal_code = models.CharField(max_length=20)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     image = models.ImageField(upload_to='location_images/')

#     def save(self, *args, **kwargs):
#         geolocator = Nominatim(user_agent="your_app_name")
#         location = geolocator.geocode(f"{self.address}, {self.city}, {self.state}, {self.country}")
#         if location:
#             self.latitude = location.latitude
#             self.longitude = location.longitude
#         super(Location, self).save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.address}, {self.city}, {self.country}"
        
# class Cart(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    noofitems=models.IntegerField()
    address=models.TextField(max_length=200)
    phone=models.CharField(max_length=200)
    order_status=models.CharField(max_length=20,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")
    date_added=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def subtotal(self):
        return self.noofitems*self.product.Amount


class Account(models.Model):
    acctnumber=models.IntegerField()
    accttype=models.CharField(max_length=200)
    balance=models.IntegerField()

    def __str__(self):
        return str(self.acctnumber)