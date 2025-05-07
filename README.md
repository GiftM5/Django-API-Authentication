# Django User Summary API

## 📌 Project Overview

**Django User Summary API** is a simple RESTful web service built with **Python**, **Django**, and the **Django REST Framework**. Its primary purpose is to serve as a secure backend endpoint that returns key information about a user's recent activity for use in a **mobile application** interface.

This application demonstrates how to:
- Build a Django-based API with authentication
- Abstract away raw SQL by using Django ORM models
- Return clean, structured, and user-friendly JSON data suitable for front-end/mobile consumption

---

## ✅ Features

- ✅ Authentication check using Django REST Framework
- ✅ Collect and return:
  - User’s **first name**
  - **Total time spent** in the app over the last 30 days
  - A list of **user transactions** from the last 30 days
- ✅ JSON response formatted for mobile applications
- ✅ Clean separation of concerns using Django’s MVC architecture

---

## 🧱 Technology Stack

| Layer         | Tool                         |
|---------------|------------------------------|
| Language      | Python 3                     |
| Web Framework | Django                       |
| API Framework | Django REST Framework (DRF)  |
| Auth System   | DRF Token or Session Auth    |
| Database ORM  | Django Models (no raw SQL)   |

---
