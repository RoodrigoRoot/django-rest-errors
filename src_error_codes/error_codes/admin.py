from django.contrib import admin
from error_codes.models import CategoryError, Error
# Register your models here.

admin.site.register(CategoryError)


class ErrorAdmin(admin.ModelAdmin):

    list_display = ("error_code", "category")


admin.site.register(Error, ErrorAdmin)

