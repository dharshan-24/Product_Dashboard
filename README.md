# Product Dashboard (Django)

## Project Overview
This project is a Product Dashboard built using Django.

Features:
- User Authentication
- Google Social Login
- Product Management
- Shopping Cart
- Checkout System

## Installation

Clone the repository

git clone https://github.com/username/product-dashboard.git

cd product-dashboard

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py migrate

Run server

python manage.py runserver

## Google Login Setup

1. Create Google OAuth Client
   
2. Add redirect URL:

http://localhost:8000/accounts/google/login/callback/

3. Add Client ID and Secret in Django Admin

## Tech Stack

Backend: Django

Database: SQLite

Frontend: HTML, CSS, Bootstrap

## Final Features Your Project Must Show

✔ Register/Login

✔ Google Login

✔ Dashboard

✔ Add Product

✔ Product List

✔ Cart

✔ Checkout

✔ Success Page

✔ Responsive UI

✔ README documentation

---

# 📁 Project Structure

product_dashboard
│
├── product_dashboard
│   ├── settings.py
│   ├── urls.py
│
├── store
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates
│       ├── dashboard.html
│       ├── add_product.html
│       ├── cart.html
│       ├── checkout.html
│       └── success.html
│
├── media
├── db.sqlite3
└── manage.py

---

# ⚙️ Setup Instructions

1️⃣ Clone Project

git clone <repository-url>

cd product_dashboard

2️⃣ Install Dependencies

pip install django

pip install django-allauth

pip install pillow

3️⃣ Run Migrations

python manage.py makemigrations

python manage.py migrate

4️⃣ Create Superuser

python manage.py createsuperuser

5️⃣ Run Server

python manage.py runserver

# Open browser:

http://127.0.0.1:8000

---

# 📊 Application Flow

Register / Login
        ↓
        
   Dashboard
        ↓
        
   Add Product
        ↓
        
   Add to Cart
        ↓
        
    Cart Page
        ↓
        
    Checkout
        ↓
        
   Success Page

---

## UI Page project

# Login Page

<img width="1920" height="1080" alt="Screenshot 2026-03-16 201923" src="https://github.com/user-attachments/assets/2e8c7d23-650a-45e6-9610-abc4d4311195" />

---

# Admin Page

<img width="1920" height="1080" alt="Screenshot 2026-03-16 201547" src="https://github.com/user-attachments/assets/52fd4b86-80cb-4e63-aa0f-d9e226ba8e2e" />


---

# Dashboard page

<img width="1920" height="1080" alt="Screenshot 2026-03-16 201636" src="https://github.com/user-attachments/assets/f77c8b43-f678-4deb-b1b3-7721feb877d7" />


---

# Product page

<img width="1920" height="1080" alt="Screenshot 2026-03-16 201609" src="https://github.com/user-attachments/assets/5e3d4cce-3c20-4b4d-9d88-dfc9bfd5cad3" />

---

#  Successfully page

<img width="1920" height="1080" alt="Screenshot 2026-03-16 201731" src="https://github.com/user-attachments/assets/9c620ba0-e2f3-4a11-9f07-44c922866b84" />













