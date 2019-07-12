from django.db import models

class Donor(models.Model):
    family_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=5)
    birth_place = models.CharField(max_length=20)
    memo = models.TextField(max_length=200)

class DonorSearch(models.Model):
    family_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=5)
    birth_place = models.CharField(max_length=20)
    memo = models.TextField(max_length=200)
