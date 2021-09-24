from django.contrib import admin
from .models import Admin,Neighborhood,Residents,Business

# Register your models here.
admin.site.register(Admin)
admin.site.register(Neighborhood)
admin.site.register(Residents)
admin.site.register(Business)