from django.contrib import admin
from .models import BannerImageModel, SignatureGeneratorModel



class BannerImageInline(admin.TabularInline):
    model = BannerImageModel
    extra = 0


class SignatureGeneratorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [BannerImageInline]
    fieldsets = (
        (None, {
            "fields": ("name", "logo",),
        }),
    )


# admin.site.register(BannerImageModel)
admin.site.register(SignatureGeneratorModel, SignatureGeneratorAdmin)