from atexit import register
import imp
from django.contrib import admin
from comp.models import Login
from import_export.admin import ImportExportModelAdmin

@admin.register(Login)
class UserAdmin(ImportExportModelAdmin):
    list_display = ("login", "password")
    pass
# Register your models here.
