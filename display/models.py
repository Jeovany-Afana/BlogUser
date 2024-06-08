from django.db import models
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')


class BlogLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)


class BlogRegister(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
