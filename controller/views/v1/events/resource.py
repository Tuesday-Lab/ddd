from rest_framework import viewsets, routers
from rest_framework.response import Response

from event.services import service as event_service
from ..events.parameter import CreateEventParameters
from ..events.schema import EventResponse


class SampleViewSet(viewsets.ViewSet):

    def create(self, request):
        # TODO: 이것도 pydantic으로??
        serializer = CreateEventParameters(data=request.data)

        serializer.is_valid(raise_exception=True)
        validate_data = serializer.validated_data
        new_event = event_service.create(title=validate_data.get("title"),
                                         slug=validate_data.get("slug"),
                                         kind=validate_data.get("kind"),
                                         amount=validate_data.get("amount"),
                                         currency=validate_data.get("currency"),
                                         max_attendee_count=validate_data.get("max_attendee_count"),
                                         description=validate_data.get("description")
                                         )
        response = EventResponse(new_event)
        return Response({"event": response.data})


router = routers.DefaultRouter()
router.register(r'', SampleViewSet, basename="events")
