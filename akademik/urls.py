from django.urls import path
from .views import MahasiswaListView, MahasiswaDetailView, PendaftaranListView,MahasiswaCreateView, PendaftaranCreateView,MahasiswaUpdateView,MahasiswaDeleteView,PendaftaranUpdateView,PendaftaranDeleteView,MataKuliahListView,MataKuliahDetailView


urlpatterns = [
    path('mahasiswa/', MahasiswaListView.as_view(), name='mahasiswa-list'),
    path('mahasiswa/<int:pk>/', MahasiswaDetailView.as_view(), name='mahasiswa-detail'),
    path('mahasiswa/tambah/', MahasiswaCreateView.as_view(), name='mahasiswa-tambah'),
    path('krs/', PendaftaranListView.as_view(), name='krs-list'),
    path('krs/tambah/', PendaftaranCreateView.as_view(), name='krs-tambah'),
    path('matakuliah/', MataKuliahListView.as_view(), name='matakuliah-list'),
    path('matakuliah/<int:pk>/', MataKuliahDetailView.as_view(), name='matakuliah-detail'),
    path('mahasiswa/<int:pk>/edit/', MahasiswaUpdateView.as_view(), name='mahasiswa-edit'),
    path('mahasiswa/<int:pk>/hapus/', MahasiswaDeleteView.as_view(), name='mahasiswa-hapus'),
    path('krs/<int:pk>/edit/', PendaftaranUpdateView.as_view(), name='krs-edit'),
    path('krs/<int:pk>/hapus/', PendaftaranDeleteView.as_view(), name='krs-hapus'),

]
