# Late Show API

A Flask REST API for managing a Late Night TV show system, built with PostgreSQL and JWT authentication.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Setup Instructions](#setup-instructions)  
- [Running the Application](#running-the-application)  
- [Authentication Flow](#authentication-flow)  
- [API Routes](#api-routes)  
- [Postman Testing](#postman-testing)  
- [GitHub Repository](#github-repository)

---

## Project Overview

This project implements a RESTful API to manage episodes, guests, appearances, and users of a Late Night TV Show. Users can register, login to get JWT tokens, and perform CRUD operations with appropriate access controls.

---

## Features

- User registration and login with JWT token authentication  
- CRUD for episodes, guests, appearances  
- Cascade delete of appearances when an episode is deleted  
- Input validation and error handling  
- Postman collection for API testing

---

## Tech Stack

- Python 3.8+  
- Flask  
- Flask SQLAlchemy  
- Flask-Migrate  
- Flask-JWT-Extended  
- PostgreSQL  
- Postman (for API testing)  

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher  
- PostgreSQL installed and running  
- pipenv or virtualenv for Python environment management

### Clone the repo

```bash
git clone https://github.com/<your_username>/late-show-api-challenge.git
cd late-show-api-challenge
