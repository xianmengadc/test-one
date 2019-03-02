from .models import User
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewset)

urlpatterns = [
    path('api/', include(router.urls))
]