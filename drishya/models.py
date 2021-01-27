from django.db import models
from django.urls import reverse
# Create your models here.


class images2(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    caption = models.TextField()
    price = models.IntegerField()
    likes = models.IntegerField()
    purchased = models.CharField(max_length=20)
    mobile_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to='images/')
class register(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    mobile_no=models.IntegerField()
    img=models.ImageField(upload_to='images/')
class addimages(models.Model):
    img=models.ImageField(upload_to='images/')    
class Profile(models.Model):
    mobile_no=models.IntegerField()
    img=models.ImageField(upload_to='images/')
    wallet=models.IntegerField()
class Adddata(models.Model):
    name=models.CharField(max_length=40)
    img_id = models.IntegerField()
class Payment(models.Model):
    card_no = models.IntegerField()
    card_name = models.CharField(max_length=50)
    amount = models.IntegerField()
class newpost(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    caption = models.TextField()
    price = models.IntegerField()
    likes = models.IntegerField()
    purchased = models.CharField(max_length=20)
    mobile_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to='images/')
def get_absolute_url(self):
    return reverse('myposts', kwargs={'pk': self.pk})
def get_absolute_url(self):
    return reverse('payment', kwargs={'pk': self.pk})
#def get_absolute_url(self):
 #   return reverse('afterpayment', kwargs={'pk': self.pk})
 