from django.db import models


class CompanyInfo(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name='Название компании'
    )

    description_about = models.TextField(
        verbose_name='О компании'
    )

    image = models.ImageField(
        upload_to='company/',
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=30
    )

    email = models.EmailField()

    address = models.CharField(
        max_length=255
    )

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'

    def __str__(self):
        return self.title