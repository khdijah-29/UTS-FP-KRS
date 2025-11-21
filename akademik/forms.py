from django import forms
from .models import Mahasiswa, Pendaftaran

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['nim', 'nama', 'jurusan']


class PendaftaranForm(forms.ModelForm):
    class Meta:
        model = Pendaftaran
        fields = ['mahasiswa', 'matakuliah', 'semester']
