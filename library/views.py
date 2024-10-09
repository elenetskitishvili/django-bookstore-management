from django.shortcuts import render
from .models import Author, Student


def home(request):
    return render(request, 'library/home.html')


def author_books_view(request):
    authors = Author.objects.all()
    return render(request, 'library/author_books.html', {'authors': authors})


def student_courses_view(request):
    students = Student.objects.all()
    return render(request, 'library/student_courses.html', {'students': students})
