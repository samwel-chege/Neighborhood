from django.contrib import admin
from .models import Profile,Neighborhood,Resident,Business,Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighborhood)
admin.site.register(Resident)
admin.site.register(Business)
admin.site.register(Post)