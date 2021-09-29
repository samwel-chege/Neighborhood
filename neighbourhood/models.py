import neighbourhood
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default="Names")
    profile_photo = models.ImageField(upload_to='photos')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username    

class Neighborhood(models.Model):
    name  = models.CharField(max_length=100) 
    location = models.CharField(max_length=100)  
    residents = models.IntegerField(default=1)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def search_neighbors(cls,search_term):
        return cls.objects.filter(name__icontains = search_term)

    @classmethod
    def update_neighbors(cls,id,resident):
        return cls.objects.filter(id=id,residents=resident)    

    def __str__(self):
        return self.name

class Resident(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='photos')
    neighbourhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def save_residents(self):
        self.save()

    def delete_residents(self):
        self.delete()

    @classmethod
    def search_resident(cls,search_term):
        return cls.objects.filter(user__username__icontains =search_term)        

    def __str__(self):
        return self.user.username
class Business(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos',default='no photo')
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=100)

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls,search_term):
        return cls.objects.filter(name__icontains = search_term)        

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post = models.TextField()
    photo = models.ImageField(upload_to='photos',default='no photo')
    neighbourhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()  

    def __str__(self):
        return self.title      




