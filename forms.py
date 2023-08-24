from django import forms
from .models import Debit, Kredit


class DebitForm(forms.ModelForm):
    class Meta:
        model = Debit
        fields = '__all__'


class KreditForm(forms.ModelForm):
    class Meta:
        model = Kredit
        fields = '__all__'
