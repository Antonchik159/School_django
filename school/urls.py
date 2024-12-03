from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subject', views.subject, name='subjects'),
    path('teacher', views.teacher, name='teachers'),
    path('student', views.student, name='students'),
    path('clas', views.clas, name='classes'),
    path('create', views.create, name='create'),
    path('shedule', views.shedule, name='shedule'),
    path('grades', views.grade, name='grades'),
    path('create_shedule', views.create_shedule, name='create_shedule'),
    path('create_teacher', views.create_teacher, name='create_teacher'),
    path('create_subject', views.create_subject, name='create_subject'),
    path('create_student', views.create_student, name='create_student'),
    path('create_grade', views.create_grade, name='create_grade')
]