from django.db import models


class University(models.Model):
    name = models.CharField(max_length=200, unique=True)
    short_name = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=100, default='Azerbaijan')
    city = models.CharField(max_length=100, default='Baku')
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'universities'
        ordering = ['name']
