from django.db import models

# Create your models here.


class Gallery(models.Model):
	decription = models.CharField(max_length=100)