from django.db import models




class Kids(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to="news/cover", null=True, blank=True)

    def __str__(self):
            return self.title


