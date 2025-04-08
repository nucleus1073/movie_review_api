# movie_review_api
This Movie Review API is a backend built with Django REST Framework (DRF) for handling movie reviews, ratings and user interactions. It offers a well-structured system for users to submit reviews, rate movies, and discover curated content.

## Table of Contents
1. [Introduction](#introduction)
2. [Core Features](#core-features)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Installation Guide](#installation-guide)
6. [Authentication System](#authentication-system)
7. [API Endpoints](#api-endpoints)
8. [Search, Filtering, and Pagination](#search-filtering-and-pagination)
9. [How to Contribute](#how-to-contribute)
10. [License][licenseDefinition]

---

## Introduction
The Movie Review API is designed for users who want to:
- Sign up and authenticate using token-based authentication.
- Submit movie reviews with ratings and read others' opinions.
- Search, filter, and paginate through movie lists and reviews seamlessly.

This API uses a custom User model, incorporates Django REST Framework for robust API handling, and applies token authentication to ensure secure access. The API is built to be adaptable for integration into different platforms, including mobile applications, websites, and other frontend interfaces.

---

## Core Features
- User Registration & Authentication: Secure user accounts with token-based authentication.
- Movie Collection Management: Store movies with titles, genres, and release dates.
- Review & Rating System: Users can submit and view movie reviews (ratings from 1 to 5 stars).
- Search & Filtering: Query movies and reviews with advanced search filters.
- Pagination Support: Optimized pagination for handling large datasets.
- Admin Dashboard: Manage users, movies, and reviews via Django’s admin panel.
- Security: Uses JWT token authentication to safeguard user interactions.

---

## Technology Stack
This project utilizes the following technologies:
- Python 3.12+: Core programming language.
- Django 5.x: Web framework for rapid API development.
- Django REST Framework (DRF): Provides API management tools.
- PostgreSQL (for production) / SQLite (for local development): Database choices.
- Django-Allauth: Handles user authentication, including social authentication.
- WhiteNoise: Manages static files in production.
- Docker (optional): Simplifies deployment via containerization.

---

## Project Structure
Here is an overview of the project’s folder structure:
```
├── movie_review_api/
│   ├── settings.py              # Django configuration
│   ├── urls.py                  # Main URL routing
│   ├── wsgi.py                  # WSGI setup for deployment
├── reviews/
│   ├── models.py                # Movie and Review models
│   ├── views.py                 # API views for handling review requests
│   ├── serializers.py           # DRF serializers for data processing
│   ├── urls.py                  # Routes for review endpoints
├── users/
│   ├── models.py                # Custom User model
│   ├── views.py                 # API views for user authentication
│   ├── serializers.py           # Serializers for user data
├── manage.py                    # Django’s management script
└── README.md                    # Documentation
```

---

## Installation Guide

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/movie-review-api.git
cd movie-review-api
```

### 2. Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables:
Create a `.env` file in the root directory with the following settings:
```bash
SECRET_KEY=your-secret-key
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Apply migrations:
```bash
python manage.py migrate
```

### 6. Create an admin user:
```bash
python manage.py createsuperuser
```

### 7. Start the development server:
```bash
python manage.py runserver
```
Now, you can access the API at `http://127.0.0.1:8000/`.

## Authentication System
The API uses Token Authentication via Django REST Framework. Users receive an authentication token upon logging in.

Include the token in API requests:
```http
Authorization: Token <your-token-here>
```

## API Endpoints

### User Routes:
- POST `/dj-rest-auth/registration/` – Register a new user.
- POST `/dj-rest-auth/login/` – Authenticate and receive a token.
- POST `/dj-rest-auth/logout/` – Logout and revoke token.

### Movie Routes:
- GET `/api/movies/` – Retrieve all movies.
- GET `/api/movies/{id}/` – Get details of a specific movie.
- POST `/api/movies/` – Add a new movie (admin only).

### Review Routes:
- GET `/api/reviews/` – Retrieve all reviews.
- POST `/api/reviews/` – Submit a review (authenticated users).
- GET `/api/reviews/{id}/` – Retrieve a single review.

## Search, Filtering, and Pagination
The API supports advanced data handling features:

- Pagination:
  - Example: `/api/movies/?limit=5&offset=10`

- Filtering:
  - Find movies by title: `/api/movies/?title=Inception`

- Searching:
  - Look up reviews by rating: `/api/reviews/?search=5`

## How to Contribute
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b new-feature`).
3. Implement your changes and commit (`git commit -m 'Added new feature'`).
4. Push the branch (`git push origin new-feature`).
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For inquiries or suggestions, feel free to reach out via email at `abrhamdanayit1995@gmail.com`.


[licenseDefinition]: #license