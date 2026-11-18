from django.db import models
from universities.models import University


class Subject(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='subjects'
    )
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    semester = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.university.short_name or self.university.name}"

    class Meta:
        db_table = 'subjects'
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(
                fields=['university', 'name'],
                name='unique_subject_per_university'
            )
        ]
