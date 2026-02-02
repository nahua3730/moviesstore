🎬 Movies Store Web Application

Movies Store is a full-stack web application built with Django that allows users to browse movies, create accounts, write reviews, and interact with community feedback in a safe and moderated environment. The project emphasizes clean backend architecture, database-driven design, and user-centered features such as review reporting and moderation.

This application was developed as part of a course project and demonstrates practical experience with Django MVC architecture, relational databases, authentication, and deployment workflows.

🚀 Features

User Authentication

User registration, login, and logout

Permission-based access to review actions

Movie Browsing

View movies and detailed movie pages

Read user-submitted reviews

Review System

Authenticated users can submit reviews

Reviews are rendered dynamically using Django templates

Review Reporting & Moderation

Users can report inappropriate reviews

Reported reviews are automatically hidden from regular users

Admins can review reported content in the Django admin panel

Admins may restore or permanently delete reviews

Responsive Interface

Built with HTML and CSS

Works across different screen sizes and devices

🛠 Tech Stack

Backend

Python

Django

Django ORM

SQLite

Frontend

HTML

CSS

Django Templates

Tools

Django Admin

Git & GitHub

🧱 Architecture

The application follows Django’s Model–View–Template (MVT) architecture:

Models define database schemas for movies, reviews, and users

Views handle request logic, permissions, and business rules

Templates render dynamic HTML pages

SQLite stores application data

The review reporting system integrates directly with the Django ORM and admin interface to support efficient moderation.

⚙️ Setup Instructions

Clone the repository

git clone <your-repository-url>
cd moviesstore


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install django


Run database migrations

python manage.py migrate


Create an admin account

python manage.py createsuperuser


Start the development server

python manage.py runserver


Application: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

🧪 Admin Moderation Workflow

A user reports a review

The review is immediately hidden from regular users

The review appears as reported in the Django admin panel

An admin can restore or permanently delete the review

This design ensures inappropriate content is handled quickly while maintaining transparency and control.

📦 Deployment Notes

The project is compatible with platforms such as PythonAnywhere

SQLite is used for simplicity and free-tier deployment support

Static files can be collected using:

python manage.py collectstatic

📚 Learning Outcomes

Full-stack Django development

Relational database modeling with SQLite

User authentication and permission handling

Content moderation workflows

Debugging routing, database, and admin configuration issues

Responsive frontend integration with backend logic

✨ Future Improvements

Search and filtering for movies

User profile pages

Enhanced UI styling

Pagination for reviews
User profile pages

Improved styling with a frontend framework

Enhanced admin dashboards
