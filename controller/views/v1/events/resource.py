from rest_framework import viewsets, routers
from rest_framework.response import Response

from ..events.parameter import SampleRequestSerializer

from ..events.schema import SampleResponseSerializer


class SampleViewSet(viewsets.ViewSet):

    def list(self, request):
        requests = SampleRequestSerializer(data=request.GET)
        requests.is_valid(raise_exception=True)

        response = SampleResponseSerializer({"text": "test"})
        return Response(response.data)


router = routers.DefaultRouter()
router.register(r'events', SampleViewSet, basename="events")
