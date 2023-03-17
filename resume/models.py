from django.db import models
from django.utils.timezone import now
import datetime

# Create your models here.
class Resume(models.Model):
    sno=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to='resume/images',default='')
    title=models.CharField(max_length=20)
    desc=models.CharField(max_length=200)
    price=models.IntegerField()
    timeStamp=models.DateTimeField(blank=True)

    

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    amount=models.IntegerField(default=0)
    r_details=models.ForeignKey(Resume,on_delete=models.CASCADE,default='')
    


class Proof(models.Model):

    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='')
    info=models.ForeignKey(Contact,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='resume/proof')
    b_date=models.DateField(auto_now_add=True)
    file=models.FileField(blank=True)
    d_date=models.DateField(auto_now_add=False,blank=True)
    status=models.BooleanField(default=False)



class User_Profile(models.Model):
    sno=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,default='')
    img=models.ImageField(upload_to='resume/profile')
    fname=models.CharField(max_length=20,default='')
    lname=models.CharField(max_length=20,default='')
    city=models.CharField(max_length=50,default='')
    gender=models.CharField(max_length=10,default='')
    email=models.CharField(max_length=50,default='')
    phone=models.CharField(max_length=13,default='')
    github_link=models.CharField(max_length=50,default='')
    linkedin_link=models.CharField(max_length=50,default='')
    college=models.CharField(max_length=100,default='')
    s_year=models.CharField(max_length=10,default='')
    e_year=models.CharField(max_length=10,default='')
    degree=models.CharField(max_length=50,default='')
    stream=models.CharField(max_length=50,default='')
    tenth_age=models.CharField(max_length=10,default='')
    twelth_age=models.CharField(max_length=10,default='')
    about=models.TextField()
    skills=models.TextField()
    achievement=models.TextField()
    projects=models.TextField()
    exprience=models.TextField()
    hobbies=models.TextField()
    other=models.TextField()
    status=models.BooleanField(default=False)



    