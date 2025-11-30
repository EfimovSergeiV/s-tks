from django.contrib import admin
from .models import EmployeesModel



class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("name", "family", "personal_phone", "work_phone", "email")
    search_fields = ("name", "family", "email")
    fieldsets = (
        (None, {
            "fields": (("name", "family"), ("personal_phone", "work_phone"), "email"),
        }),
    )


admin.site.register(EmployeesModel, EmployeesAdmin)