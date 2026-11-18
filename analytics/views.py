
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Count

from universities.models import University
from subjects.models import Subject
from materials.models import Material
from quizzes.models import Quiz, QuizResult
from voting.models import Vote, Report


def analytics_dashboard(request):
    total_users = User.objects.count()
    total_universities = University.objects.count()
    total_subjects = Subject.objects.count()
    total_materials = Material.objects.count()
    total_quizzes = Quiz.objects.count()
    total_quiz_results = QuizResult.objects.count()
    total_votes = Vote.objects.count()
    total_reports = Report.objects.count()

    popular_subjects = (
        Subject.objects
        .values('id', 'name')
        .annotate(material_count=Count('materials'))
        .order_by('-material_count')[:5]
    )

    recent_materials = (
        Material.objects
        .select_related('subject', 'uploaded_by')
        .order_by('-created_at')[:5]
    )

    context = {
        'total_users': total_users,
        'total_universities': total_universities,
        'total_subjects': total_subjects,
        'total_materials': total_materials,
        'total_quizzes': total_quizzes,
        'total_quiz_results': total_quiz_results,
        'total_votes': total_votes,
        'total_reports': total_reports,
        'popular_subjects': popular_subjects,
        'recent_materials': recent_materials,
    }

    return render(request, 'analytics/dashboard.html', context)
