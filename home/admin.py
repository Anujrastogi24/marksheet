from django.contrib import admin
from .models import stud,marks
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(stud)
class studData(ImportExportModelAdmin):
    pass

@admin.register(marks)
class studMarks(ImportExportModelAdmin):
    pass