from django.db import models


# Create your models here.
class Engineering_colleges(models.Model):
    College_Name= models.CharField(max_length=150)
    Fee = models.CharField(max_length=100)
    Exam = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    Img = models.CharField(max_length=500)
    Rating= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Medical_colleges(models.Model):
    College_Name= models.CharField(max_length=150)
    Fee = models.CharField(max_length=100)
    Exam = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    Img = models.CharField(max_length=500)
    Rating= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Management_colleges(models.Model):
    College_Name= models.CharField(max_length=150)
    Fee = models.CharField(max_length=100)
    Exam = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    Img = models.CharField(max_length=500)
    Rating= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Design_colleges(models.Model):
    College_Name= models.CharField(max_length=150)
    Fee = models.CharField(max_length=100)
    Exam = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    Img = models.CharField(max_length=500)
    Rating= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Science_colleges(models.Model):
    College_Name= models.CharField(max_length=150)
    Fee = models.CharField(max_length=100)
    Exam = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    Img = models.CharField(max_length=500)
    Rating= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Law_colleges(models.Model):
    College_Name= models.CharField(max_length=150)
    Fee = models.CharField(max_length=100)
    Exam = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    Img = models.CharField(max_length=500)
    Rating= models.CharField(max_length=50)

    def __str__(self):
        return self.name
