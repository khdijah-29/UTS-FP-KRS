from django.contrib import admin
from .models import Mahasiswa, MataKuliah, Pendaftaran

admin.site.register(Mahasiswa)
admin.site.register(MataKuliah)
admin.site.register(Pendaftaran)
