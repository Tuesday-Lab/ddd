from django.conf.urls import url, include
from .events.resource import router as events_resource

urls = [
    url(r'v1/', include(events_resource.urls)),
]
