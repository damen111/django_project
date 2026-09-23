from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Car(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.IntegerField()
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Studentt(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name