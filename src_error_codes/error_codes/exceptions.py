from rest_framework.exceptions import APIException
from rest_framework import status
from error_codes.functions import (get_error_code, check_fields,
                                    create_body_response_error, exists_error_code,
                                    get_fields_errors)


class CustomErrorException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "A error occurred."

    def __init__(self, error_code: str=None, static_fields=None):
        if exists_error_code(error_code):
            object_error = get_error_code(error_code)
            if check_fields(get_fields_errors()):
                body = create_body_response_error(object_error, static_fields)
                self.detail = body
        else:
            new_detail = {'message': self.message, 'error_code': "001"}
            if static_fields:
                new_detail.update(static_fields)
            self.detail = new_detail


