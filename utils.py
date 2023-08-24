from .models import Debit, Kredit
from django.db.models import Sum


def get_saldo(siswa):
    debit = Debit.objects.filter(siswa=siswa).aggregate(Sum('nominal'))
    kredit = Kredit.objects.filter(siswa=siswa).aggregate(Sum('nominal'))
    saldo = debit['nominal__sum'] - kredit['nominal__sum']
    return saldo
