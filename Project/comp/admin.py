from atexit import register
import imp
from django.contrib import admin
from comp.models import Users
from import_export.admin import ImportExportModelAdmin

@admin.register(Users)
class UserAdmin(ImportExportModelAdmin):
    list_display = ("login", "password")
    pass
# Register your models here.
