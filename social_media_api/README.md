# Social Media API

This is a basic Social Media API built with Django and Django REST Framework. It allows user registration, login, and profile management with token-based authentication.

---

## **Installation**

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd social_media_api

### 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install django djangorestframework djangorestframework-authtoken pillow

Setup

1. Run migrations
python manage.py makemigrations
python manage.py migrate

2. Create a superuser ( for admin access)
python manage.py createsuperuser

Running the Server

Start the development server:

python manage.py runserver

API Endpoints
1. Register a new user

URL: /auth/register/

Method: POST

Request Body:

{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}


Response:

{
  "user": {
    "id": 1,
    "username": "your_username",
    "email": "your_email@example.com",
    "bio": "",
    "profile_picture": null,
    "followers": []
  },
  "token": "your_token_here"
}

2. Login user

URL: /auth/login/

Method: POST

Request Body:

{
  "username": "your_username",
  "password": "your_password"
}


Response:

{
  "token": "your_token_here"
}

3. View / Update Profile

URL: /auth/profile/

Method: GET / PUT

Headers:

Authorization: Token your_token_here


GET Response:

{
  "id": 1,
  "username": "your_username",
  "email": "your_email@example.com",
  "bio": "Your bio",
  "profile_picture": null,
  "followers": []
}


PUT Request Body Example:

{
  "bio": "Updated bio"
}
```
