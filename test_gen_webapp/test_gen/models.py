from django.db import models
from authentication.models import user
# Create your models here.

class user_questionnaire(models.Model):
    user_id= models.ForeignKey(user,on_delete=models.CASCADE)
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField()

class question_options(models.Model):
    question_id = models.ForeignKey(user_questionnaire,on_delete=models.CASCADE)
    option_id = models.AutoField(primary_key=True)
    question_option = models.TextField()

    