from django.db import models


class EmployeesModel(models.Model):
    """ Модель сотрудников компании """

    name = models.CharField(max_length=100, verbose_name="Имя")
    family = models.CharField(max_length=100, verbose_name="Фамилия")
    personal_phone = models.CharField(max_length=20, verbose_name="Личный телефон")
    work_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Рабочий телефон")
    email = models.EmailField(null=True, blank=True, verbose_name="Электронная почта")
    class Meta:
        verbose_name = "Сотрудника"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.name} {self.family}"