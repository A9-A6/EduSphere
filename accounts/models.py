from django.db import models
from django.contrib.auth.models import User
from universities.models import University


class Profile(models.Model):

    ROLE_CHOICES = [
        ('STUDENT', 'Student'),
        ('PROFESSOR', 'Professor'),
        ('UNIVERSITY_ADMIN', 'University Administrator'),
        ('PLATFORM_ADMIN', 'Platform Administrator'),
        ('MODERATOR', 'Content Moderator'),
    ]

    LANGUAGE_CHOICES = [
        ('AZ', 'Azerbaijani'),
        ('EN', 'English'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    university = models.ForeignKey(
        University,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members'
    )

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default='STUDENT'
    )

    preferred_language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default='AZ'
    )

    student_id = models.CharField(
        max_length=50,
        blank=True
    )

    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    class Meta:
        db_table = 'user_profiles'
