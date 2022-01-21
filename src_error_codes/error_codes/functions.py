from typing import List, Dict
from django.apps import apps as django_app
from django.conf import settings
from django.db.models import Model
from error_codes.ownexceptions import FieldsDoesNotExists
from error_codes.models import Error, CategoryError


def exists_error_code(error_code: str) -> bool:
    return get_error_model().objects.filter(error_code__icontains=error_code).exists()


def get_error_code(error_code: str) -> Error:
    obj_error_code = get_error_model().objects.filter(error_code__icontains=error_code).first()
    return obj_error_code


def get_error_model() -> Model:
    return django_app.get_model(get_model_error_from_settings(), require_ready=False)

def get_model_error_from_settings():
    ERROR_MODEL = "error_codes.Error"
    try:
        MODEL_TO_USE = settings.ERROR_MODEL
    except Exception:
        MODEL_TO_USE = ERROR_MODEL
    return MODEL_TO_USE

def get_fields_error_models() -> List:
    data = []
    error_model = get_error_model()
    fields_model = error_model._meta.fields
    for field in fields_model:
        data.append(field.name)
    return data


def check_fields(fields) -> bool:
    fields_models = get_fields_error_models()
    for field in fields:
        if not field in fields_models:
            raise FieldsDoesNotExists(f"The field: '{field}' does not exists in the table")
    return True


def create_body_response_error(error_object: Model, static_fields = None) -> Dict:
    error_response = {}
    for field in get_fields_errors():
        field_object = error_object._meta.get_field(field)
        error_response[field] = field_object.value_from_object(error_object)
    if static_fields:
        error_response.update(static_fields)
        return error_response
    return error_response


def category_all() -> List[CategoryError]:
    return CategoryError.objects.all()


def get_category_by_name(name: str) -> CategoryError:
    return CategoryError.objects.get(name=name)


def get_fields_errors():
    DEFAULT_ERROR_MODEL_FIELDS = ['error_code', 'message']
    try:
        ERROR_TO_USE = settings.ERROR_MODEL_FIELDS
    except Exception:
        ERROR_TO_USE = DEFAULT_ERROR_MODEL_FIELDS
    return ERROR_TO_USE

