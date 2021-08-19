from django.db import models
import re
from datetime import date

# Create your models here.

class UserValidator(models.Manager):
    def registerValidator(self, postData):
        errors={}
        email_regex= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #emails = User.objects.email()
        existing_users = User.objects.filter(email=postData['email'])
        todays_date= date.today()
        if not email_regex.match(postData['email']):
            errors['format'] = "Please submit a valid email"
        if len(postData['lname']) < 2:
            errors['lname'] = "Please submit a name of at least 2 characters"
        if len(postData['fname']) < 2:
            errors['fname'] = "Please submit a name of at least 2 characters"
        if len(postData['email']) < 7:
            errors['email'] = "Please submit a valid email"
        elif len(postData['email']) >= 7:
            if len(existing_users) > 0:
                errors['unique'] = "This email already exists in our database"
        if len(postData['password']) < 8:
            errors['password'] = "Please submmit a password of at least eight characters"
        if postData['password'] != postData['cpassword']:
            errors['confirm'] = "Passwords do not match"
        if postData['birthday'] > str(todays_date):
            errors['birthday'] = "Birthday must be in the past"
        #if postData['birthday'][0:4] > str((int(date.today.year) -13)):
            #errors['youth'] = "User must be at least 13 years old" 
        return errors



class User(models.Model):
    fname=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=200)
    birthday=models.DateTimeField()
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
    objects=UserValidator()

