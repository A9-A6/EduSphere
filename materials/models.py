from django.db import models
from django.contrib.auth.models import User
from subjects.models import Subject


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'material_categories'
        ordering = ['name']


class Material(models.Model):

    LANGUAGE_CHOICES = [
        ('AZ', 'Azerbaijani'),
        ('EN', 'English'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    file = models.FileField(upload_to='materials/')

    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default='AZ'
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='materials'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='materials'
    )

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='uploaded_materials'
    )

    downloads = models.PositiveIntegerField(default=0)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'materials'
        ordering = ['-created_at']