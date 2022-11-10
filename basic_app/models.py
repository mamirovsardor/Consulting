
from django.db import models

# Create your models here.

class Services(models.Model):
    img = models.ImageField(upload_to='images/',null=True, blank=True)
    name = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self) :
        return self.name

class Facts(models.Model):
    name = models.CharField(max_length=60) 
    number = models.CharField(max_length=60)
    def __str__(self) :
        return self.name

class Team(models.Model):
    img = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=89)
    prof = models.CharField(max_length=89)
    des = models.TextField()

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField(max_length=80) 
    price =  models.CharField(max_length=80)
    month =  models.CharField(max_length=80)
    addition1 = models.CharField(max_length=80)
    addition2 = models.CharField(max_length=80)
    addition3 = models.CharField(max_length=80)
    addition4 = models.CharField(max_length=80)
    addition5 = models.CharField(max_length=80)

    def __str__(self) :
        return self.name



class Blog(models.Model):
    img = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=89)
    date = models.CharField(max_length=89)
    des = models.TextField()
    # des2 = models.TextField()
    

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    img = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=89)
    des = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone=models.CharField(max_length=40)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Yevropa(models.Model):
    img = models.ImageField(upload_to="images/")
    img2 = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self
    
    
    
class Blog2(models.Model):
    img = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=89)
    des = models.TextField()
    des2 = models.TextField()
    
    img2 = models.ImageField(upload_to="images/")
    img3 = models.ImageField(upload_to="images/")
    img4 = models.ImageField(upload_to="images/")
    des3 = models.TextField()
    des4 = models.TextField()
    name2 = models.CharField(max_length=100)
    des5 = models.TextField()
    
    

    def __str__(self):
        return self.name
    
    
class comment(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name