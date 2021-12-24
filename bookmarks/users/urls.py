# Core django imports
from django.urls import path

# Imports from your apps
# from dubs2.usuarios.views import LoginAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UsuarioViewSet)

urlpatterns = [
    path('login/', DubsLoginView.as_view(), name='login'),
] + router.urls