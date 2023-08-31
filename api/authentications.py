from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ValidationError
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.utils.translation import gettext_lazy as _
from siswa.models import Siswa
from ..models import Tenan


class KartuSiswaAuthentication(BaseAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "IDCard ".  For example:

        Authorization: IDCard {id_siswa}:{id_perangkat}
    """

    keyword = 'IDCard'
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth:
            raise exceptions.AuthenticationFailed(_('Invalid id card header. No credentials provided.'))

        if auth[0].lower() != self.keyword.lower().encode():
            raise exceptions.AuthenticationFailed(_('Invalid keyword in header.'))

        if len(auth) == 1:
            msg = _('Invalid id card header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid id card header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            key = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid id card header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(key)

    def authenticate_credentials(self, key):
        try:
            id_siswa, id_perangkat = key.split(":")
        except ValueError:
            raise exceptions.AuthenticationFailed(_("Invalid Key"))

        try:
            siswa = Siswa.objects.get(id=id_siswa)
        except (Siswa.DoesNotExist, ValidationError):
            raise exceptions.AuthenticationFailed(_('Invalid ID Card.'))

        try:
            Tenan.objects.get(id_perangkat=id_perangkat)
        except (Tenan.DoesNotExist, ValidationError):
            raise exceptions.AuthenticationFailed(_('Invalid ID Perangkat.'))

        return AnonymousUser(), siswa
