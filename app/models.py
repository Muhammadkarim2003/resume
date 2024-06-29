from django.db import models

# Create your models here.

class Men(models.Model):
    full_name = models.CharField(max_length=300)
    kasb = models.CharField(max_length=300)


    def __str__(self) -> str:
        return self.full_name



class ContactInfo(models.Model):
    tel_number = models.CharField(max_length=13)
    telegram = models.URLField()
    email = models.EmailField()
    github = models.URLField()
    location = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.tel_number

class About_me(models.Model):
    about_me = models.TextField()

    def __str__(self) -> str:
        return self.about_me

class Skills(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class AvatarImage(models.Model):
    image = models.ImageField(upload_to='avatars/')

    
