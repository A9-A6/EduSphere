from django.db import models
from django.contrib.auth.models import User
from materials.models import Material


class Vote(models.Model):

    VOTE_CHOICES = [
        (1, 'Upvote'),
        (-1, 'Downvote'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='material_votes'
    )

    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='votes'
    )

    vote_type = models.SmallIntegerField(
        choices=VOTE_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.material.title}'

    class Meta:
        db_table = 'material_votes'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'material'],
                name='unique_user_material_vote'
            )
        ]


class Report(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('REVIEWED', 'Reviewed'),
        ('RESOLVED', 'Resolved'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='material_reports'
    )

    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='reports'
    )

    reason = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report: {self.material.title}'

    class Meta:
        db_table = 'material_reports'
        ordering = ['-created_at']