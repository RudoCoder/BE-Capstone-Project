# Job Creation in Africa (JCIA) - BackEnd

This is the backend API for the Job Creation in Africa platform, a system designed to bridge the gap between university graduates, employers, and organizations offering opportunities.
The API is built with Django REST Framework (DRF) and provides endpoints for authentication, graduate registration, company job postings, and scholarship management.
**With this API, the aim is to empower African graduates by connecting them with meaningful employment and opportunities for growth.**

# Features
User Registration & Authentication

Role-based users: Graduate, Company, Organization

JWT Authentication with djangorestframework-simplejwt

Graduate Features

Automatic GraduateProfile creation on registration

Manage profiles, skills, and academic history

Company Features

Post, update, and manage job opportunities

Search and filter graduates

Organization Features

Offer scholarships and learning opportunities

Track applicants

Security

JWT-based token authentication

Role-based access control

CORS-enabled for frontend integration

# Tech Stack
Backend Framework: Django, Django REST Framework

Database: PostgreSQL (recommended)

Authentication: SimpleJWT

Other Tools:

django-cors-headers – CORS management

python-dotenv – Environment variables

# Installation & Setup
```bash
# 1) Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 2) Install deps
pip install "Django>=4.2" djangorestframework djangorestframework-simplejwt drf-yasg django-cors-headers

# 3) Start project & apps
django-admin startproject jobboard .
python manage.py startapp users
python manage.py startapp graduates
python manage.py startapp jobs
python manage.py startapp scholarships
python manage.py startapp applications

# 4) Create the files as shown below (overwrite placeholders)

# 5) Migrate & run
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # follow prompts
python manage.py runserver
```
Step 1: Run your Django server

Open your terminal:
```bash
# Activate your virtual environment if not already
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Run the Django server
python manage.py runserver


Your API will now be available at:

http://127.0.0.1:8000/
```
Step 2: Register a user

Endpoint: POST /api/auth/register/
Purpose: Create a new user

Open Postman → New Request → POST
```bash
URL:

http://127.0.0.1:8000/api/auth/register/


Body → raw → JSON:

{
  "username": "zali",
  "email": "zali@example.com",
  "password": "Passw0rd!",
  "role": "graduate"
}
```

Send the request.
You should see something like:
```bash
{
  "id": 1,
  "username": "zali",
  "email": "zali@example.com",
  "role": "graduate"
}
```
Step 3: Log in (get JWT token)

Endpoint: POST /api/auth/token/
Purpose: Authenticate user and get a token

Postman → New Request → POST
```bash
URL:

http://127.0.0.1:8000/api/auth/token/


Body → raw → JSON:

{
  "username": "zali",
  "password": "Passw0rd!"
}
```

Send request → Response should contain:
```bash
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

Important: Copy the access token. You’ll use it for authorized requests.

Step 4: View your profile

Endpoint: GET /api/profile/
Purpose: Retrieve your graduate profile (auto-created for graduates)

Postman → New Request → GET
```bash
URL:

http://127.0.0.1:8000/api/profile/
```

Authorization → Bearer Token → Paste your access_token

Send request → Response example:
```bash
{
  "id": 1,
  "university": "",
  "degree": "",
  "skills": "",
  "cv_file": ""
}
```
Step 5: Update your profile

Endpoint: PUT /api/profile/
Purpose: Edit your graduate profile

Postman → New Request → PUT
```bash
URL:

http://127.0.0.1:8000/api/profile/
```

Authorization → Bearer Token

Body → raw → JSON:
```bash
{
  "university": "University of Zimbabwe",
  "degree": "BSc Cybersecurity",
  "skills": "Python, Django, Networking",
  "cv_file": "http://example.com/cv.pdf"
}
```

Send → You should get updated profile data in the response.

Step 6: Create a job post (as company user)

Create a new company user in Postman via /api/auth/register/
```bash
{
  "username": "company1",
  "email": "company@example.com",
  "password": "Passw0rd!",
  "role": "company"
}
```

Login → Get access_token for the company.

Endpoint: POST /api/jobs/
```bash
{
  "title": "Backend Developer",
  "description": "Build APIs with Django",
  "requirements": "Python, Django, REST",
  "location": "Harare"
}
```

Authorization → Bearer Token → company’s token

Send → Response should show created job:
```bash
{
  "id": 1,
  "title": "Backend Developer",
  "description": "Build APIs with Django",
  "requirements": "Python, Django, REST",
  "location": "Harare",
  "created_at": "...",
  "updated_at": "..."
}
```
Step 7: View job posts (public)

Endpoint: GET /api/jobs/
No auth needed. You should see the list of job posts.

Step 8: Create a scholarship (as organization user)

Create an organization user via /api/auth/register/

Login → Get token

Endpoint: POST /api/scholarships/
```bash
{
  "title": "Tech Scholarship 2025",
  "description": "Full tuition for top students",
  "eligibility_criteria": "BSc students only",
  "deadline": "2025-09-01"
}
```

Authorization → Bearer Token → organization token

Send → Response should show the scholarship created.

Step 9: Apply to a job or scholarship (as graduate)

Endpoint: POST /api/applications/create/

Apply to a job:
```bash
{
  "job": 1
}


Apply to a scholarship:

{
  "scholarship": 1
}
```

Authorization → Bearer Token → graduate’s token

Response shows your application created.

Step 10: View applications

Graduate view: GET /api/applications/ → see your own applications

Company/org view: GET /api/applications/manage/ → see applications to your job/scholarship posts

Step 11: Test Swagger docs (optional)

Open in browser:
```bash
http://127.0.0.1:8000/api/docs/
```

## Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
source venv/Scripts/activate      # Windows (Git Bash / PowerShell)
```
## Install dependencies
```bash
pip install -r requirements.txt
```
## Setup environment variables

Create a .env file in the root directory:
```bash
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/jobdb
```
## Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
## Create a superuser
```bash
python manage.py createsuperuser
```
## Start the development server
```bash
python manage.py runserver
```

# API Endpoints

**Authentication**

POST /api/register/ – Register a new user (Graduate, Company, or Organization)

POST /api/token/ – Obtain JWT access/refresh tokens

POST /api/token/refresh/ – Refresh token

**Graduate**

GET /api/me/ – View logged-in user details

GET /api/graduate/profile/ – Get graduate profile

PUT /api/graduate/profile/ – Update graduate profile

**Company**

POST /api/company/jobs/ – Post a new job

GET /api/company/jobs/ – List company jobs

**Organization**

POST /api/scholarships/ – Create scholarship opportunity

GET /api/scholarships/ – List scholarships

# Future Improvements
- Advanced search & recommendation system using AI

- Resume/CV parsing for graduates

- Job application tracking for companies

- Scholarship matching engine

## Clone Repo
```bash
https://github.com/RudoCoder/BE-Capstone-Project.git
```

