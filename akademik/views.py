from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import MahasiswaForm, PendaftaranForm
from .models import Mahasiswa, Pendaftaran,MataKuliah
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import MahasiswaSerializer, MataKuliahSerializer, PendaftaranSerializer
from rest_framework import viewsets



class MahasiswaListView(ListView):
    model = Mahasiswa
    template_name = "akademik/mahasiswa_list.html"


class MahasiswaDetailView(DetailView):
    model = Mahasiswa
    template_name = "akademik/mahasiswa_detail.html"


class PendaftaranListView(ListView):
    model = Pendaftaran
    template_name = "akademik/pendaftaran_list.html"


class MahasiswaCreateView(CreateView):
    model = Mahasiswa
    form_class = MahasiswaForm
    template_name = "akademik/mahasiswa_form.html"
    success_url = reverse_lazy('mahasiswa-list')


class PendaftaranCreateView(CreateView):
    model = Pendaftaran
    form_class = PendaftaranForm
    template_name = "akademik/pendaftaran_form.html"
    success_url = reverse_lazy('krs-list')


class MahasiswaUpdateView(UpdateView):
    model = Mahasiswa
    form_class = MahasiswaForm
    template_name = "akademik/mahasiswa_form.html"
    success_url = reverse_lazy('mahasiswa-list')


class MahasiswaDeleteView(DeleteView):
    model = Mahasiswa
    template_name = "akademik/mahasiswa_confirm_delete.html"
    success_url = reverse_lazy('mahasiswa-list')


class PendaftaranUpdateView(UpdateView):
    model = Pendaftaran
    form_class = PendaftaranForm
    template_name = "akademik/pendaftaran_form.html"
    success_url = reverse_lazy('krs-list')


class PendaftaranDeleteView(DeleteView):
    model = Pendaftaran
    template_name = "akademik/pendaftaran_confirm_delete.html"
    success_url = reverse_lazy('krs-list')


class MahasiswaListAPI(ListAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

class MahasiswaDetailAPI(RetrieveAPIView):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer


class MataKuliahListAPI(ListAPIView):
    queryset = MataKuliah.objects.all()
    serializer_class = MataKuliahSerializer

class MataKuliahDetailAPI(RetrieveAPIView):
    queryset = MataKuliah.objects.all()
    serializer_class = MataKuliahSerializer


class PendaftaranListAPI(ListAPIView):
    queryset = Pendaftaran.objects.all()
    serializer_class = PendaftaranSerializer

class PendaftaranDetailAPI(RetrieveAPIView):
    queryset = Pendaftaran.objects.all()
    serializer_class = PendaftaranSerializer

class MahasiswaViewSet(viewsets.ModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer
    basename = 'api-mahasiswa'


class MataKuliahViewSet(viewsets.ModelViewSet):
    queryset = MataKuliah.objects.all()
    serializer_class = MataKuliahSerializer
    basename = 'api-matakuliah'


class PendaftaranViewSet(viewsets.ModelViewSet):
    queryset = Pendaftaran.objects.all()
    serializer_class = PendaftaranSerializer    
    basename = 'api-pendaftaran'