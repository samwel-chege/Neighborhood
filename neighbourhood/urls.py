from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    path('create-admin',views.create_admin,name='create-admin'),
    path('create-hood/(\d+)',views.create_hood,name='create-hood'),
    path('add-resident/',views.add_resident,name='add-resident'),
    path('update-hood/',views.update_hood,name='update-hood'),
    path('all-residents/',views.all_residents,name='all-residents'),
    path('business/',views.business,name='business'),
    path(r'^posts/(\d+)',views.post,name='post'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)