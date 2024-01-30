from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    # Other location attributes

class Category(models.Model):
    name = models.CharField(max_length=255)

class Tour(models.Model):
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True)
    # Other tour attributes

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, null=True, blank=True)
    # Other review attributes

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    # Other booking attributes


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True)
    # Other comment attributes

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    # Other payment attributes
