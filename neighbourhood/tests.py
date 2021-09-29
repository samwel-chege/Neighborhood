from django.test import TestCase
from django.contrib.auth.models import User
from .models import Neighborhood, Profile, Amenity, Post, Neighbourhood, Resident, Business

class ProfileTestClass(TestCase):
    def setUp(self):
        self.sammie = User(username = "sammie", email = "sammie@gmail.com",password = "1234")
        self.profile = Profile(user= self.sammie)
        self.sammie.save()
        self.profile.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.sammie, User))
        self.assertTrue(isinstance(self.profile, Profile))

class ResidentTestClass(TestCase):
    def setUp(self):
        self.sammie = User(username = "sammie", email = "sammie@gmail.com",password = "1234")
        self.resident = Resident(user= self.sammie, profile_photo='mepng')
        self.sammie.save()
        self.resident.save()

    def tearDown(self):
        Resident.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.sammie, User))
        self.assertTrue(isinstance(self.resident, Resident))

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.location = Neighborhood(location= self.loresho,residents=2)
        self.westlands.save()
        self.location.save()

    def tearDown(self):
        Neighborhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.loresho, Neighborhood))

class BusinessTestClass(TestCase):
    def setUp(self):
        self.sammie = User(username = "sammie", email = "sammie@gmail.com",password = "1234")
        self.business = Business(user= self.sammie, photo='mepng')
        self.sammie.save()
        self.business.save()

    def tearDown(self):
        Business.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.sammie, User))
        self.assertTrue(isinstance(self.business, Business))    

        