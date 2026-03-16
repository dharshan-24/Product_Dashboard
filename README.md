# Product Dashboard (Django)

## Project Overview

The Product Dashboard is a web application built using Python and Django that allows users to manage products and simulate a simple shopping experience.

The system provides features such as user authentication, Google social login, product management, cart functionality, and checkout process. The goal of the project is to demonstrate how a basic e-commerce workflow can be implemented using Django.

Users can securely register or log in to the platform, add products to the dashboard, and manage them through a simple interface. Products can then be added to a shopping cart and processed through a checkout flow that ends with a confirmation success page.

The backend of the application is built using Django, which handles authentication, database operations, and routing. The application uses SQLite as the database to store product data. User authentication is enhanced with Google OAuth integration using django-allauth.

The frontend is implemented using HTML and CSS, and it follows responsive UI principles inspired by the provided design kit.

# Features:
- User Authentication
  
- Google Social Login
  
- Product Management
  
- Shopping Cart
  
- Checkout System

## Installation

Clone the repository

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
# Cart Page

<img width="1920" height="1080" alt="Screenshot 2026-03-16 203731" src="https://github.com/user-attachments/assets/e3dd5dbf-afe7-4763-b1db-b065a1905d23" />

---

# CheckOut page

<img width="1920" height="1080" alt="Screenshot 2026-03-16 203854" src="https://github.com/user-attachments/assets/8666ed41-f501-44d6-86d3-91c3dcc3045f" />

---

#  Successfully page

<img width="1920" height="1080" alt="Screenshot 2026-03-16 201731" src="https://github.com/user-attachments/assets/9c620ba0-e2f3-4a11-9f07-44c922866b84" />













