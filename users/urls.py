from django.conf.urls import url
from users import views
from rest_framework import serializers, viewsets, routers
from django.conf.urls import url, include
from django.contrib.auth.models import User


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
         url(r'^', include(router.urls)),
         url(r'contact', views.contact, name='contact'),
         url(r'login', views.user_login, name='login'),
         url(r'register', views.register, name='register')
         ]
