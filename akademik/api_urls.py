from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MahasiswaViewSet, MataKuliahViewSet, PendaftaranViewSet

router = DefaultRouter()
router.register(r'mahasiswa', MahasiswaViewSet)
router.register(r'matakuliah', MataKuliahViewSet)
router.register(r'pendaftaran', PendaftaranViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
