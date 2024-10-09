from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authors-books/', views.author_books_view, name='author_books'),
    path('students-courses/', views.student_courses_view, name='student_courses'),
]
