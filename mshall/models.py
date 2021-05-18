from django.db import models

# Create your models here.

class Gallerypics(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)

class Champs2020to2021tech(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)

class Champs2019to2020socult(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)

class Champs2019to2020tech(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)

class Champs2018to2019sports(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)

class Champs2017to2018sports(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)

class Champs2016to2017sports(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)

class Champs2012to2013socult(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)

class Champs2011to2012sports(models.Model):
    img = models.ImageField(upload_to='pictures')
    medal = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    competition = models.CharField(max_length=75)
    field = models.CharField(max_length=75)