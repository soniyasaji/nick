from django.db import models

#table definition
class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    price=models.IntegerField()
    pdf=models.FileField(upload_to="book/pdf")
    image=models.ImageField(upload_to="book/cover",null=True,blank=True)

    def __str__(self):
        return self.title






