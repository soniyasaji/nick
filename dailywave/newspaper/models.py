from django.db import models
class Newspaper(models.Model):
    news_title=models.CharField(max_length=200)
    news_desc=models.TextField()
    news_price=models.IntegerField()
    news_pdf=models.FileField(upload_to="news/pdf")
    news_image=models.ImageField(upload_to="news/cover", null=True, blank=True)

    def __str__(self):
        return self.news_title

class News_Type(models.Model):
    ntypname=models.CharField(max_length=200)
    ndesc=models.TextField()
    nimage=models.ImageField(upload_to='newspaper/type',null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    newsc=models.ForeignKey(Newspaper,on_delete=models.CASCADE)
    stock=models.IntegerField()
    navailable=models.BooleanField(default=True)
    ncreated=models.DateTimeField(auto_now_add=True)
    nupdated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ntypname

class Video(models.Model):

    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')



    class Meta:
        verbose_name='Video'
        verbose_name_plural = 'Videos'