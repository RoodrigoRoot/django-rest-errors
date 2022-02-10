from django.contrib import admin
from error_codes.models import CategoryError, Error
from django.conf import settings
# Register your models here.

try:
    MODEL_ERROR = settings.MODEL_ERROR
except Exception as e:
    MODEL_ERROR = Error


admin.site.register(CategoryError)


class ErrorAdmin(admin.ModelAdmin):

    list_display = ("error_code", "category")


admin.site.register(MODEL_ERROR, ErrorAdmin)
