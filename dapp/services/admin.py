from django.contrib import admin
from .models import BannerImageModel, CatalogModel, SignatureGeneratorModel



class BannerImageInline(admin.TabularInline):
    model = BannerImageModel
    extra = 0


class CatalogsInline(admin.TabularInline):
    model = CatalogModel
    extra = 0


class SignatureGeneratorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [BannerImageInline, CatalogsInline]
    fieldsets = (
        (None, {
            "fields": ("name", "logo",),
        }),
    )



admin.site.register(SignatureGeneratorModel, SignatureGeneratorAdmin)