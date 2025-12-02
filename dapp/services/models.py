from django.db import models



class SignatureGeneratorModel(models.Model):
    """ EMAIL Signature Generator Model """
    
    name = models.CharField(max_length=255, verbose_name="Название шаблона")
    logo = models.ImageField(upload_to='signatures/logos/', default="https://tehnosvar.ru/media/redactor/2022/08/29/tehoras-1.png", blank=True, null=True, verbose_name="Логотип справа", help_text="Разрешение лого = 185x162px")

    class Meta:
        verbose_name = "Шаблон подписи email"
        verbose_name_plural = "Шаблоны подписи email"

    def __str__(self):
        return self.name


class BannerImageModel(models.Model):
    """ Изображение баннера в подписи email """

    signature = models.ForeignKey(SignatureGeneratorModel, on_delete=models.CASCADE, related_name="banner_images")
    link = models.URLField(max_length=500, verbose_name="Ссылка на сайт")    
    image = models.ImageField(upload_to='signatures/banners/', verbose_name="Изображение баннера 600x100(px)")

    class Meta:
        verbose_name = "Изображение баннера внизу подписи"
        verbose_name_plural = "Изображения баннеров внизу подписи"

    def __str__(self):
        return f"Banner Image {self.link}"
    

class CatalogModel(models.Model):
    """ Ссылки на каталоги в подписи """
    
    signature = models.ForeignKey(SignatureGeneratorModel, on_delete=models.CASCADE, related_name="catalogs")
    icon = models.ImageField(upload_to='signatures/catalogs/icons/', verbose_name="Иконка каталога", help_text="")
    name = models.CharField(max_length=255, verbose_name="Название каталога")
    link = models.URLField(max_length=500, verbose_name="Ссылка на каталог")

    class Meta:
        verbose_name = "Ссылку на каталог"
        verbose_name_plural = "Ссылки на каталоги"

    def __str__(self):
        return self.name