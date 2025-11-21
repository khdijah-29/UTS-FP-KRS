from rest_framework import serializers
from .models import Mahasiswa, MataKuliah, Pendaftaran

class MahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ['id', 'nim', 'nama', 'jurusan']


class MataKuliahSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataKuliah
        fields = ['id', 'kode_mk', 'nama_mk', 'sks', 'dosen']


class PendaftaranSerializer(serializers.ModelSerializer):
    mahasiswa = MahasiswaSerializer(read_only=True)
    matakuliah = MataKuliahSerializer(read_only=True)

    class Meta:
        model = Pendaftaran
        fields = ['id', 'mahasiswa', 'matakuliah', 'semester', 'nilai']
