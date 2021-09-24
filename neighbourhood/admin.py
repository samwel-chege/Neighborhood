from django.contrib import admin
from .models import Admin,Neighborhood,Resident,Business

# Register your models here.
admin.site.register(Admin)
admin.site.register(Neighborhood)
admin.site.register(Resident)
admin.site.register(Business)