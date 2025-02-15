from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet
from .views import dashboard

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard, name='dashboard'),
]