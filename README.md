# MySite Django Polls Application

## Description

A simple polls app created using Django. A full-featured polling application built with Django that allows users to create polls, vote on questions, and view real-time results. This project demonstrates core Django concepts including models, views, templates, forms, and user authentication.

**Importance:** Serves as an educational example of Django web development and can be extended for real-world polling needs.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Credits](#credits)
- [License](#license)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

## Local Setup

1. **Clone the repository**
1a) git clone
https://github.com/JustinJay7/project-Dango-polls.git

2. **Create virtual environment**

2a) python -m venv venv #Linux/Mac
2b) source venv/bin/activate 
           # OR
venv\Scripts\activate   #Windows
  
3. **Install dependencies**
   
3a) pip install -r requirements.txt

4. **Database setup**
   
4a) python manage.py migrate
   
5. **Create superuser (optional)**
   
5a) python manage.py createsuperuser
   
6. **Run development server**
   
   python manage.py runserver
   

## Usage

## **Access the Application**

1. Start the server: python manage.py runserver
2. Open your browser to: http://localhost:8000
3. Navigate through the application:

**Key Features in Action**

· View Polls: Browse available polls on the home page
· Vote: Select choices and submit votes
· Results: See real-time voting results
· Admin Panel: Manage polls at http://localhost:8000/admin

## Screenshots

### [Home](screenshots/home.png)
[![Home Page](screenshots/home.png)](screenshots/home.png)
*Landing page showing available polls*

### [Voting](screenshots/vote.png)  
[![Voting Page](screenshots/vote.png)](screenshots/vote.png)
*Interface for submitting votes on poll questions*

### [Results](screenshots/results.png)
[![Results Page](screenshots/results.png)](screenshots/results.png)
*Real-time visualization of poll results*

### [Admin](screenshots/admin.png)
[![Admin Panel](screenshots/admin.png)](screenshots/admin.png)
*Django admin interface for managing polls*
## Features

· ✅ User authentication system
· ✅ Poll creation and management
· ✅ Real-time voting mechanism
· ✅ Results visualization
· ✅ Responsive web design
· ✅ Django admin interface
· ✅ REST API endpoints

## API Endpoints

· GET /api/polls/ - List all polls
· POST /api/vote/ - Submit a vote
· GET /api/results/<poll_id>/ - Get poll results

## Credits

*Author*

· Justin Jay - GitHub Profile

*Technologies Used*

· Django - Web framework
· SQLite - Database (development)
· HTML/CSS - Frontend structure and styling
· JavaScript - Interactive features

## **Acknowledgments**

· Django documentation and community
· Bootstrap for UI components

## **License**

This project is licensed under the MIT License - see the LICENSE file for details.
