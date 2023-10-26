from django.db import models

# Create your models here.
# Table for Partner Requests page .
class PartnerRequest(models.Model):
    sno = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=40)
    # address = models.CharField(max_length=30)
    restaurantname = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=70)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Request from " + self.restaurantname + "owner" + "--" + self.fullname