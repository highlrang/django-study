from rest_framework.response import Response
from .dtos import ApiResponse, ErrorCode
from rest_framework.views import exception_handler
from rest_framework.utils import json
from rest_framework import serializers

class ApiException(Exception):

    def __init__(self, error_code):
        self.error_code = error_code

    def __str__(self):
        return self.error_code.code + ' ' + self.error_code.message
        

def custom_exception_handler(exception, context):
    
    if(isinstance(exception, ApiException)):
        data = ApiResponse.fail(exception.error_code)
    else:
        response = exception_handler(exception, context)
        message = response.data['detail'] if 'detail' in response.data.keys() else response.data
        data = ApiResponse(response.status_code, message)

    return Response(data.__dict__)
    
    