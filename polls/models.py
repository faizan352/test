from django.forms import ModelForm
from django.db import models
from django import forms
# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=30)


class students(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)



class Users(models.Model):
    name = models.CharField(max_length=20)

class TaskDetails(models.Model):
    objects = ModelForm
    Users = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    typ = models.CharField(max_length=20)
    due_date = models.DateTimeField(max_length=20)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    priority = models.TextField(max_length=20)
    assign_to = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)

class CommentTask(models.Model):
    TaskDetails = models.ForeignKey(TaskDetails, on_delete=models.CASCADE)
    Users = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    parent_id = models.IntegerField()


class Csv(models.Model):
    std_rollno = models.IntegerField(max_length=20)
    std_name = models.CharField(max_length=20)
    std_gender = models.CharField(max_length=20)
    std_mail = models.CharField(max_length=20)











