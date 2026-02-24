Club Connect

Club Connect is a Django-based social platform designed for college clubs and student communities.
It allows users to register, share posts, interact through likes and comments, and manage role-based access for club administrators.

🚀 Features
🔐 Authentication System

User registration and login

Custom role: Club Admin

Admin approval workflow for Club Admin accounts

Inactive accounts cannot log in until approved

📝 Posts

Create posts (Club Admin only)

Upload images with captions

Like posts

Comment on posts

👤 User Profiles

Profile picture support

Bio section

User post grid

Post count and total likes statistics

🛡 Admin Approval Flow

Users requesting Club Admin role are set as is_active = False

Redirected to an Approval Pending page

Superuser activates account via Django Admin panel

🎨 UI Features

Sticky navigation bar

Responsive layout

Animated post cards

Modern profile layout

Approval pending page design

🛠 Tech Stack

Backend: Django 4.2

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django DB)

Authentication: Django built-in auth system

Version Control: Git & GitHub

📂 Project Structure
clubconnect/
│
├── core/               # Main app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── register.html
│   ├── login.html
│   ├── profile.html
│   ├── approval_pending.html
│
├── static/
├── manage.py
└── db.sqlite3
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/nilarpan-dev/club_connect.git
cd club-connect
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

If requirements.txt is not available:

pip install django
4. Apply Migrations
python manage.py makemigrations
python manage.py migrate
5. Create Superuser
python manage.py createsuperuser
6. Run Server
python manage.py runserver

Open:

http://127.0.0.1:8000/
🔑 Admin Access

Visit:

http://127.0.0.1:8000/admin/

From the admin panel you can:

Approve Club Admin accounts

Manage users

Manage posts and comments

📌 Future Improvements

Follow / follower system

Notifications

Post detail page

Edit profile feature

Deployment (Render / Railway / AWS)

REST API integration

📜 License

This project is for educational purposes and can be modified or extended as needed.
