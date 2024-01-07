from rest_framework import status, views
from rest_framework.response import Response

from core.utils import get_geoip_from_request


class MyGeoIPApiView(views.APIView):
    """
    ApiView для получения текущей геолокации клиента.
    Геолокация берется по IP из request.
    """
    def get(self, request):
        geoip = get_geoip_from_request(request)
        if geoip is None:
            return Response(
                {"geoip_error": "Произошла ошибка при получении геолокации."},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            geoip,
            status=status.HTTP_200_OK
        )
