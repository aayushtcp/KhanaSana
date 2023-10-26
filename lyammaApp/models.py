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
    
    
class AllItems(models.Model):
    sno = models.AutoField(primary_key=True)
    itemname = models.CharField(max_length=50)
    category = models.CharField(max_length=100) # fiter by set comprehension
    price = models.IntegerField(blank=True, null=True) #convert to integer in js
    image = models.ImageField(upload_to="lyammaApp/images", default="upload-image")
    explain = models.CharField(max_length=232) #optional
    slug = models.CharField(max_length=130, default="this-s") # url management
    
    def __str__(self):
        return "Item " + self.itemname + "Category" + "--" + self.category