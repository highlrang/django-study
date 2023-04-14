
from dataclasses import dataclass
from enum import Enum

class ApiResponse:

    def __init__(self, code=None, message=None, data=None):
        self.code = code
        self.message = message
        self.data = data

    @staticmethod
    def success(data):
        return ApiResponse(message="success", data=data)
    
    @staticmethod
    def fail(error_code):
        return ApiResponse(code=error_code.code, message=error_code.message)


class ErrorCode(Enum):
    DATA_NOT_FOUND = ("DATA_NOT_FOUND", "데이터를 찾을 수 없습니다.")

    def __init__(self, code, message):
        self.code = code
        self.message = message


