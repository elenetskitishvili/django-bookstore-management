from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.title)


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)


class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return str(self.name)

    def list_courses(self):
        return ', '.join(course.name for course in self.courses.all())
