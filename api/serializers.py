from rest_framework import serializers
from siswa.models import Siswa


class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = '__all__'
