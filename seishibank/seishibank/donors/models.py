from django.db import models

BLOOD=(("0","A-"),("1","A+"),("2","AB-"),("3","AB+"),("4","B-"),("5","B+"),("6","O-"),("7","O+"))
HAIR=(("0","ダークブラウン"),("1","ダークブロンド"),("2","ブラウン"),("3","ブラウン"),("4","ブロンド"),("5","黒色"),("6","赤色"))
HEIGHT = (("0","-159"),("1","160-169"),("2","170-179"),("3","180-189"),("4","190-"))
WEIGHT = (("0","-50"),("1","50-59"),("2","60-69"),("3","70-79"),("4","80-89"),("5","90-"))
ICI_IUI = (("0","ICI-未洗浄"),("1","IUI-洗浄済"))

class Donor(models.Model):
    number = models.CharField(max_length=20)
    hair_color = models.CharField(max_length=20,verbose_name="Hair Color", choices=HAIR)
    height = models.CharField(max_length=20,verbose_name="Height(cm)", choices=HEIGHT)
    weight = models.CharField(max_length=20,verbose_name="Weight(kg)", choices=WEIGHT)
    ICI_IUI = models.CharField(max_length=20,verbose_name="ICI_IUI", choices=ICI_IUI)
    blood_type = models.CharField(max_length=20,verbose_name="Blood Type", choices=BLOOD)
    memo = models.TextField(max_length=200)

class DonorSearch(models.Model):
    family_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=5)
    birth_place = models.CharField(max_length=20)
    memo = models.TextField(max_length=200)
