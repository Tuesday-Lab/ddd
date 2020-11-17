from django.conf.urls import include, url

from .resource import router as users_resource

urls = [
    url(r'', include(users_resource.urls)),
]
