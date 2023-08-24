from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel


class Debit(BaseModel):
    siswa = models.ForeignKey("siswa.Siswa", on_delete=models.CASCADE)
    nominal = models.DecimalField(decimal_places=2, max_digits=12)
    petugas = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.siswa} - {self.nominal}"


class Kredit(BaseModel):
    siswa = models.ForeignKey("siswa.Siswa", on_delete=models.CASCADE)
    nominal = models.DecimalField(decimal_places=2, max_digits=12)
    petugas = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.siswa} - {self.nominal}"
