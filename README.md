# Bookstore Management - Django Learning Project

This project is a learning exercise that focuses on understanding Django model relationships, methods, and properties.

## Project Tasks

### Task 1: ForeignKey Relationship

- **Models Created**: `Author` and `Book`
- Added a `ForeignKey` field in the `Book` model to link it to the `Author` model.
- Implemented a method in the `Author` model to count the number of books associated with each author.

### Task 2: ManyToManyField Implementation

- **Models Created**: `Student` and `Course`
- Added a `ManyToManyField` in the `Student` model to associate it with multiple `Course` instances.
- Implemented a method in the `Student` model to list all the courses a student is enrolled in.

### Task 3: Using Model Properties

- Added a `date_of_birth` field to the `Student` model.
- Created a property in the `Student` model that calculates and returns the student's age.

## What I Learned

- How to create Django models with `ForeignKey` and `ManyToManyField` relationships.
- How to use model methods to retrieve and display related data.
- How to use model properties to calculate and present information.
- Working with Django's admin interface for managing data.
- Using Django's template system to render data in a user-friendly way.
