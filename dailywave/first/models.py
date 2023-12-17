from django.db import models

class First(models.Model):
    first_title=models.CharField(max_length=200)
    first_desc=models.TextField()
    first_image=models.ImageField(upload_to="news/cover", null=True, blank=True)

    def __str__(self):
        return self.first_title


