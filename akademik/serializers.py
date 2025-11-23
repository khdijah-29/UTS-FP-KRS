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
    # Menampilkan detail mahasiswa & matakuliah ketika GET (read)
    mahasiswa = MahasiswaSerializer(read_only=True)
    matakuliah = MataKuliahSerializer(read_only=True)

    # Memungkinkan input ID mahasiswa & matakuliah ketika POST/PUT (write)
    mahasiswa_id = serializers.PrimaryKeyRelatedField(
        queryset=Mahasiswa.objects.all(),
        source="mahasiswa",
        write_only=True
    )
    matakuliah_id = serializers.PrimaryKeyRelatedField(
        queryset=MataKuliah.objects.all(),
        source="matakuliah",
        write_only=True
    )

    class Meta:
        model = Pendaftaran
        fields = ['id', 'mahasiswa', 'matakuliah', 'semester', 'mahasiswa_id', 'matakuliah_id']
