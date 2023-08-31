from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel


class VIA(models.TextChoices):
    WEB = "web", "Web"
    API = "api", "API"


class Debit(BaseModel):
    siswa = models.ForeignKey("siswa.Siswa", on_delete=models.CASCADE)
    nominal = models.DecimalField(decimal_places=2, max_digits=12)
    petugas = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    via = models.CharField(max_length=10, choices=VIA.choices, default=VIA.WEB)
    extra_data = models.TextField(blank=True, null=True,
                                  help_text="bisa diisi untuk melengkapi request yang diterima")

    def __str__(self):
        return f"{self.siswa} - {self.nominal}"


class Kredit(BaseModel):
    siswa = models.ForeignKey("siswa.Siswa", on_delete=models.CASCADE)
    nominal = models.DecimalField(decimal_places=2, max_digits=12)
    petugas = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    via = models.CharField(max_length=10, choices=VIA.choices, default=VIA.WEB)
    extra_data = models.TextField(blank=True, null=True,
                                  help_text="bisa diisi untuk melengkapi request yang diterima")

    def __str__(self):
        return f"{self.siswa} - {self.nominal}"


class Tenan(BaseModel):
    nama = models.CharField(max_length=220)
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    sekolah = models.ForeignKey("sekolah.Sekolah", on_delete=models.SET_NULL, null=True,
                                help_text="Pilih jika tenan berada pada sekolah mana")
    id_perangkat = models.CharField(max_length=150, unique=True,
                                    help_text="ID dapat ditemukan pada bagian bawah perangkat")
    jenis = models.CharField(max_length=150, blank=True, null=True,
                             help_text="Jenis dapat ditemukan pada bagian bawah perangkat, jika tidak ditemukan "
                                       "bisa dikosongkan")

    def __str__(self):
        return f"{self.nama} - {self.sekolah.nama}"


class Transaksi(BaseModel):
    no_transaksi_tenan = models.CharField(max_length=100, help_text="no ini didapatkan dari sistem pembayaran tenan")
    tenan = models.ForeignKey(Tenan, on_delete=models.CASCADE)
    kredit = models.ForeignKey(Kredit, on_delete=models.CASCADE)
    nominal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.no_transaksi_tenan} - {self.tenan} - {self.nominal}"
