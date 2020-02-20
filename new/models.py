from django.forms import ModelForm
from django.db import models
from django import forms
# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=30)