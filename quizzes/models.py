from django.db import models
from django.contrib.auth.models import User
from subjects.models import Subject


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='quizzes'
    )

    time_limit = models.PositiveIntegerField(default=30)
    passing_score = models.PositiveIntegerField(default=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'quizzes'
        ordering = ['-created_at']


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    question_text = models.TextField()
    points = models.PositiveIntegerField(default=1)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.question_text[:100]

    class Meta:
        db_table = 'quiz_questions'
        ordering = ['order']


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )

    answer_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    class Meta:
        db_table = 'quiz_answers'


class QuizResult(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='quiz_results'
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='results'
    )

    score = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    total_questions = models.PositiveIntegerField(default=0)
    correct_answers = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"

    class Meta:
        db_table = 'quiz_results'
        ordering = ['-completed_at']
