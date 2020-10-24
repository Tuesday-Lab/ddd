from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


# from rest_framework.views import exception_handler


# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.
#     response = exception_handler(exc, context)
#
#     # Now add the HTTP status code to the response.
#     if response is not None:
#         response.data['status_code'] = response.status_code
#
#     return response
#
#
# class BaseException(Exception):
#     status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#     error_code = 500
#     message = "Server Error"
#
#     def __init__(self, error_code=None, message=None):
#         self.error_code = error_code
#         self.message = message
#
#         self.detail = f"[{self.error_code}] {self.message}"
#
#     def __str__(self):
#         return str(self.detail)


class ConflictResource(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = _('conflict')
    default_code = 'conflict with resource'
