from django.db import models



class SignatureGeneratorModel(models.Model):
    """ EMAIL Signature Generator Model """
    
    name = models.CharField(max_length=255, verbose_name="Название шаблона")
    logo = models.ImageField(upload_to='signatures/logos/', blank=True, null=True, verbose_name="Логотип справа", help_text="Разрешение лого = 185x162px")

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