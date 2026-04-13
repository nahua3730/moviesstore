# 🎬 Movies Store Web Application

**Movies Store** is a full-stack web application built with Django that allows users to browse movies, create accounts, write reviews, and interact with community feedback in a moderated environment.

This project demonstrates experience with Django architecture, relational databases, authentication systems, and deployment workflows.

## 🚀 Features

### 🔐 User Authentication
- User registration, login, and logout  
- Permission-based access control for review actions  

### 🎥 Movie Browsing
- Browse a list of movies  
- View detailed movie pages  
- Read user-submitted reviews  

### ✍️ Review System
- Authenticated users can submit reviews  
- Reviews rendered dynamically using Django templates  

### 🚨 Review Reporting & Moderation
- Users can report inappropriate reviews  
- Reported reviews are automatically hidden from regular users  
- Admins can manage reports via the Django admin panel  
- Admins can restore or permanently delete reviews  

### 📱 Responsive Interface
- Built with HTML and CSS  
- Works across different screen sizes and devices  

---

## 🛠 Tech Stack

### Backend
- Python  
- Django  
- Django ORM  
- SQLite  

### Frontend
- HTML  
- CSS  
- Django Templates  

### Tools
- Django Admin  
- Git & GitHub  

---

## 🧱 Architecture

The application follows Django’s **Model–View–Template (MVT)** architecture:

- **Models**: Define database schemas for movies, reviews, and users  
- **Views**: Handle request logic, permissions, and business rules  
- **Templates**: Render dynamic HTML pages  
- **Database**: SQLite stores application data  

The review moderation system is integrated with Django ORM and the admin interface.

---

## ⚙️ Setup Instructions

1. Clone the Repository
```bash
git clone <your-repository-url>
cd moviesstore
```

2. Create Virtual Environment
```bash
python -m venv venv
```

3. Activate Virtual Environment
```bash
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

4. Install Dependencies
```bash
pip install django
```

5. Run Migrations
```bash
python manage.py migrate
```

6. Create Superuser
```bash
python manage.py createsuperuser
```

7. Run Development Server
```bash
python manage.py runserver
```

App: http://127.0.0.1:8000/  
Admin Panel: http://127.0.0.1:8000/admin/  

---

## 🧪 Admin Moderation Workflow

- A user reports a review  
- The review is automatically hidden from regular users  
- The review appears as reported in the admin panel  
- Admin chooses to:
  - Restore the review, or  
  - Permanently delete it  

---

## 📦 Deployment Notes

- Compatible with platforms such as PythonAnywhere  
- SQLite used for simplicity and free-tier deployment  

```bash
python manage.py collectstatic
```

---

## ✨ Future Improvements

- Search and filtering for movies  
- User profile pages  
- Improved UI styling (frontend framework)  
- Pagination for reviews  
- Enhanced admin dashboards  
