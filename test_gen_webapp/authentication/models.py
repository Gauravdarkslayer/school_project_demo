from django.db import models

# Create your models here.

roles = (("stu","student"),("org","organization"),("schl","school"))
class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name= models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    role = models.CharField(choices=roles,max_length=50)
