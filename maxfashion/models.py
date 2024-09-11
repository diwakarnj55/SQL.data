from django.db import models

class Jewellery(models.Model):
    jel_item=models.TextField(max_length=100)
    jel_rate=models.TextField(max_length=100)
    jel_image=models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return self.jel_item
class Checkout(models.Model):
    Firstname=models.TextField(max_length=50)
    Lastname=models.TextField(max_length=50)
    Emailaddress=models.TextField(max_length=50)
    phonenumber=models.TextField(max_length=50)
    Addressline1=models.TextField(max_length=200)
    Addressline2=models.TextField(max_length=200)
    country=models.TextField(max_length=50, blank=True)
    region=models.TextField(max_length=50, blank=True)
    def __str__(self):
        return self.Firstname

    

