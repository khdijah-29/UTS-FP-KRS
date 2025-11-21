from django.db import models

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=12, unique=True)
    nama = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama} ({self.nim})"


class MataKuliah(models.Model):
    kode_mk = models.CharField(max_length=10, unique=True)
    nama_mk = models.CharField(max_length=100)
    sks = models.IntegerField()
    dosen = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.kode_mk} - {self.nama_mk}"


class Pendaftaran(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, related_name='krs')
    matakuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, related_name='pendaftaran')
    semester = models.CharField(max_length=10)
    nilai = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.mahasiswa.nama} - {self.matakuliah.nama_mk}"
