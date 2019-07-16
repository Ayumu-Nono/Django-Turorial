from django.db import models

HAIR=(("0","ダークブラウン"),("1","ダークブロンド"),("2","ブラウン"),("3","ブラウン"),("4","ブロンド"),("5","黒色"),("6","赤色"))
HEIGHT = (("0","-159"),("1","160-169"),("2","170-179"),("3","180-189"),("4","190-"))
WEIGHT = (("0","-50"),("1","50-59"),("2","60-69"),("3","70-79"),("4","80-89"),("5","90-"))
ICI_IUI = (("0","ICI-未洗浄"),("1","IUI-洗浄済"))
BLOOD=(("0","A-"),("1","A+"),("2","AB-"),("3","AB+"),("4","B-"),("5","B+"),("6","O-"),("7","O+"))
TODAY_PHOTO = (("0","いいえ"),("1","はい"))
PROFILE = (("0","ドナー独占権"),("1","基本"),("2","詳細"))
EYE_COLOR = (("0","灰色"),("1","青色"),("2","青色/灰色"),("3","青色/緑色"),("4","茶色"),("5","茶色/灰色"),("6","茶色/緑色"),("7","緑色"),("8","緑色/灰色"))
MOT = (("0","MOT5"),("1","MOT10"),("2","MOT20"),("3","MOT30"),("4","MOT40"),("5","MOT50+"))

class Donor(models.Model):
    number = models.CharField(max_length=20,verbose_name="ID")
    hair_color = models.CharField(max_length=20,verbose_name="髪の色", choices=HAIR)
    height = models.CharField(max_length=20,verbose_name="身長(cm)", choices=HEIGHT)
    weight = models.CharField(max_length=20,verbose_name="体重(kg)", choices=WEIGHT)
    ICI_IUI = models.CharField(max_length=20,verbose_name="ICI/IUI", choices=ICI_IUI)
    blood_type = models.CharField(max_length=20,verbose_name="血液型", choices=BLOOD)
    today_photo = models.CharField(max_length=20,verbose_name="現在の写真", choices=TODAY_PHOTO)
    profile = models.CharField(max_length=20,verbose_name="プロフィール", choices=PROFILE)
    eye_color = models.CharField(max_length=20,verbose_name="瞳の色", choices=EYE_COLOR)
    mot = models.CharField(max_length=20,verbose_name="運動能力", choices=MOT)


    
    memo = models.TextField(max_length=200)

class DonorSearch(models.Model):
    family_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=5)
    birth_place = models.CharField(max_length=20)
    memo = models.TextField(max_length=200)
