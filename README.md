# LogESP - Security Information and Event Management (SIEM) System

**LogESP** is a lightweight, Django-based SIEM (Security Information and Event Management) system designed for centralized log collection, real-time monitoring, rule-based alerting, and simple threat detection using customizable parsers and correlation rules.

## Features

- Log ingestion and search
- Custom parsing and event categorization
- Alert system with severity levels
- Admin panel for managing rules, alerts, IPs, etc.
- Dashboard and navigation interface
- Email notifications for high-severity alerts
- Modular design using Django framework

## Technologies Used

- Python (Django Framework)
- SQLite (default, can be extended)
- HTML/CSS (Bootstrap for UI)
- JavaScript (basic interactivity)
- Admin panel (Django built-in)

## Project Structure

LogESP/
│
├── siem/ # Main Django app
│ ├── models.py # Database models
│ ├── views.py # View logic
│ ├── urls.py # App routes
│ ├── templates/ # HTML templates
│ ├── static/ # CSS/JS and styling
│
├── templates/ # Global templates (admin, login, etc.)
├── static/ # Global static files
├── db.sqlite3 # Default SQLite database
├── manage.py # Django management file
└── README.md # Project description


## Setup Instructions

1. **Clone the repository:**
   
   git clone https://github.com/your-username/logesp.git
   cd logesp
Install dependencies:

pip install -r requirements.txt
Run migrations and start the server:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Create admin user
python manage.py runserver
Access the application:

Admin Panel: http://127.0.0.1:8000/admin/

Dashboard: http://127.0.0.1:8000/

Author
D.M.V.Nimna
Final Year Student, BSc(hons) Computer Security
NSBM Green University, Plymouth University
Supervised by: Dr. Pabudi Abeyrathne
 











