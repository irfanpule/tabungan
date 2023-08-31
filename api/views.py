from rest_framework.response import Response
from rest_framework.views import APIView
from .authentications import KartuSiswaAuthentication
from ..utils import get_saldo
from .serializers import SiswaSerializer


class CekSaldoAPIVIew(APIView):
    authentication_classes = [KartuSiswaAuthentication]

    def get(self, request):
        siswa = request.auth
        saldo = get_saldo(siswa)
        content = {
            'siswa': SiswaSerializer(siswa, read_only=True).data,
            'saldo': str(saldo)
        }
        return Response(content)
