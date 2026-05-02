from django.contrib import admin
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from .models import BannerImageModel, CatalogModel, SignatureGeneratorModel, AccessConfModel



class BannerImageInline(admin.TabularInline):
    model = BannerImageModel
    extra = 0


class CatalogsInline(admin.TabularInline):
    model = CatalogModel
    extra = 0


class SignatureGeneratorAdmin(admin.ModelAdmin):
    change_form_template = "admin/services/signaturegeneratormodel/change_form.html"
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [BannerImageInline, CatalogsInline]
    fieldsets = (
        (None, {
            "fields": ("name", "logo",),
        }),
    )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<path:object_id>/duplicate/",
                self.admin_site.admin_view(self.duplicate_view),
                name="services_signaturegeneratormodel_duplicate",
            ),
        ]
        return custom_urls + urls

    @transaction.atomic
    def duplicate_view(self, request, object_id):
        if request.method != "POST":
            self.message_user(request, "Копирование доступно только через кнопку в форме.", level=messages.WARNING)
            return HttpResponseRedirect(reverse("admin:services_signaturegeneratormodel_change", args=[object_id]))

        if not self.has_add_permission(request):
            self.message_user(request, "Недостаточно прав для создания копии.", level=messages.ERROR)
            return HttpResponseRedirect(reverse("admin:services_signaturegeneratormodel_changelist"))

        source_object = self.get_object(request, object_id)
        if source_object is None:
            self.message_user(request, "Объект для копирования не найден.", level=messages.ERROR)
            return HttpResponseRedirect(reverse("admin:services_signaturegeneratormodel_changelist"))

        duplicated_object = SignatureGeneratorModel.objects.get(pk=source_object.pk)
        duplicated_object.pk = None
        duplicated_object.save()

        for banner in source_object.banner_images.all():
            banner.pk = None
            banner.signature = duplicated_object
            banner.save()

        for catalog in source_object.catalogs.all():
            catalog.pk = None
            catalog.signature = duplicated_object
            catalog.save()

        self.message_user(request, "Точная копия успешно создана.", level=messages.SUCCESS)
        return HttpResponseRedirect(
            reverse(
                "admin:services_signaturegeneratormodel_change",
                args=[duplicated_object.pk],
            )
        )






admin.site.register(SignatureGeneratorModel, SignatureGeneratorAdmin)
admin.site.register(AccessConfModel)