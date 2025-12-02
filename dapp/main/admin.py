from django.contrib import admin
from .models import EmployeesModel



class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("name", "mobile", "work_phone", "email")
    search_fields = ("name", "email")
    fieldsets = (
        (None, {
            "fields": (("name", "job"), ("mobile", "work_phone"), ("whatsapp", "telegramm"), "email"),
        }),
    )


admin.site.register(EmployeesModel, EmployeesAdmin)