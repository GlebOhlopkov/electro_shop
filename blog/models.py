from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    slug = models.CharField(max_length=150, verbose_name='slug')
    text = models.TextField(verbose_name='text')
    image = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    is_published = models.BooleanField(default=True, verbose_name='is_published')
    views_count = models.IntegerField(default=0, verbose_name='views_count')

    def __str__(self):
        return f'{self.title}, {self.created_at}, views: {self.views_count}'

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
