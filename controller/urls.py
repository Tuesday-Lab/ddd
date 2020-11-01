from django.conf.urls import url, include

from .views import v1
from .views.v1.events.resource import router as events_resource
from .views.v1.users.resource import router as users_resource

urlpatterns = [
    url(r'v1/events/', include(events_resource.urls)),
    url(r'v1/users/', include(users_resource.urls)),
]
