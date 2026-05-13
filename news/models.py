from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    preview_text = models.TextField(blank=True)
    full_text = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('title',)
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
    