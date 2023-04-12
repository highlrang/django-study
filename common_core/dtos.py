
from dataclasses import dataclass

class ApiResponse:

    def __init__(self, status=0, message="", data=None):
        self.status = status
        self.message = message
        self.data = data

    @staticmethod
    def success(data):
        return ApiResponse(200, "success", data)
    
    @staticmethod
    def fail(message):
        return ApiResponse(500, message)