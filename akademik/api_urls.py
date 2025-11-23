from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MahasiswaViewSet, MataKuliahViewSet, PendaftaranViewSet

router = DefaultRouter()
router.register(r'mahasiswa', MahasiswaViewSet, basename = 'api-mahasiswa')
router.register(r'matakuliah', MataKuliahViewSet, basename = 'api-matakuliah')
router.register(r'pendaftaran', PendaftaranViewSet, basename = 'api-pendaftaran')

urlpatterns = [
    path('', include(router.urls)),
]
