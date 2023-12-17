from django.db import models



class Magazine(models.Model):
    mag_title=models.CharField(max_length=200)
    mag_desc=models.TextField()
    mag_price=models.IntegerField()
    mag_pdf=models.FileField(upload_to="news/pdf")
    mag_image=models.ImageField(upload_to="news/cover", null=True, blank=True)

    def __str__(self):
        return self.mag_title



