from django.conf.urls import url, include
from .resource import router as events_resource

urls = [
    url(r'', include(events_resource.urls)),
]
