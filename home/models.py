from django.db import models
from django.utils import timezone
from datetime import date,datetime,timedelta
from django.contrib.auth.models import User
# # Create your models here.


class Post(models.Model):
    id =models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    image = models.ImageField(blank=True,null=True,upload_to='home/images')
    author=models.CharField(max_length=14)
    date = models.DateField(default=date.today)
    slug=models.CharField(max_length=130)
    content=models.TextField()

    def __str__(self):
        return self.title+' '+self.author

class Volunteer(models.Model):
    id =models.AutoField(primary_key=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100,blank=True)
    emailid = models.EmailField(blank=True,max_length=255)
    phone_no = models.BigIntegerField()
    address=models.TextField(blank=True,null=True)
    content=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.fname + ' ' + self.lname

class MedicineDonation(models.Model):
    id =models.AutoField(primary_key=True)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100,blank=True)
    address=models.TextField(blank=True,null=True)
    phone_no = models.BigIntegerField(blank=True)
    med = models.CharField(max_length=100)
    md = models.DateField(default=date.today)
    ed = models.DateField(default=date.today)
    quantity=models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.med

class PostComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username +' '+ self.post.title

class Doctor(models.Model):
    id =models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    type_of_doc = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    state=models.CharField(max_length=100,blank=True)    
    is_doc = models.BooleanField(default=False)
    reg_id = models.CharField(max_length=200)

    def __str__(self):
        return self.name +' '+ self.type_of_doc
    
class Session(models.Model):
    id =models.AutoField(primary_key=True)
    doc=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    type_of_session = models.CharField(max_length=100)
    meeting_url = models.URLField(max_length=500)
    date = models.DateField(default=date.today)
    st = models.TimeField()
    et = models.TimeField()

    def __str__(self):
        return self.doc.user.username + self.type_of_session
