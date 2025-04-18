# 🏫 ClubConnect – University Club Portal

**ClubConnect** is a simple Django-based web portal built to help students browse university clubs, view events, see members, and read announcements. Admins can manage all data through the Django admin panel. This project focuses on models, views, URLs, and templates — no forms or user authentication.

---

## 📌 Project Objective

Create a basic university club portal where:

- Students can browse clubs and view their details.
- Each club has events, members, and announcements.
- Admins manage all content through Django Admin.
- A special view shows **this week's events**.

---

## 🧱 Features & Tech Coverage

| Feature                         | Included |
|--------------------------------|----------|
| Models (Club, Event, etc.)     | ✅ Yes   |
| Views (List & Detail)          | ✅ Yes   |
| URL Routing                    | ✅ Yes   |
| Templates (basic HTML)         | ✅ Yes   |
| Admin Panel CRUD               | ✅ Yes   |
| Forms / Auth                   | ❌ No    |
| Static files (optional)        | ✅ Yes   |

---

## 🧩 Models

### 1. `Club`
- `name` (CharField)
- `description` (TextField)
- `founded_date` (DateField)

### 2. `Member`
- `club` (ForeignKey to Club)
- `name`
- `role` (e.g., President, Member)
- `join_date`

### 3. `Event`
- `club` (ForeignKey to Club)
- `title`
- `description`
- `date`

### 4. `Announcement`
- `club` (ForeignKey to Club)
- `title`
- `message`
- `posted_on`

---

## 🗂 Pages Implemented

| URL                       | Description                                        |
|---------------------------|----------------------------------------------------|
| `/clubs/`                 | List all clubs (name + short description)          |
| `/clubs/<int:id>/`        | Club detail page: members, events, announcements   |
| `/events/`                | List all events                                    |
| `/announcements/`         | List all recent announcements                      |
| `/this-week/`             | 🔥 Shows only events happening this week (Mon–Sun) |

---
## ✨ Special Feature: This Week's Events

A view is implemented to display only the events happening this week (Monday to Sunday).  
You can access this view at:  
---
## 👨‍💻 How to Use

### 1. Clone & Setup
```bash
git clone https://github.com/yourusername/clubconnect.git
cd clubconnect
python manage.py migrate
python manage.py runserver


