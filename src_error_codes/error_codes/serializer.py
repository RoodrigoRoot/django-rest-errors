from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from error_codes.exceptions import CustomErrorException
from error_codes.functions import get_fields_errors
from django.conf import settings


class OverrideSerializer(serializers.Serializer):

    def is_valid(self, raise_exception=False):
        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )

        if not hasattr(self, '_validated_data'):
            override_exception = False
            try:
                self._validated_data = self.run_validation(self.initial_data)
            except ValidationError as ex:
                self._validated_data = []
                self._errors = ex.detail
            except CustomErrorException as exc:
                override_exception = True
                self._validated_data = []
                self._errors = exc.detail
            else:
                self._errors = []

        if self._errors and raise_exception:
            if override_exception:
                if self._errors:
                    error_dict = {}
                    for field in get_fields_errors():
                        error_dict[field] = self.errors.pop(field)
                    raise CustomErrorException(error_dict["error_code"], self.errors)
                raise CustomErrorException()
            raise ValidationError(self.errors)
        return not bool(self._errors)
