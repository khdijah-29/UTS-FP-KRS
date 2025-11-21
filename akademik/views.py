from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import MahasiswaForm, PendaftaranForm
from .models import Mahasiswa, Pendaftaran


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
