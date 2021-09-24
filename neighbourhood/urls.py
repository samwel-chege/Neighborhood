from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)