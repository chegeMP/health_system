## Documentation

- [Health App Presentation](./assets/presentations/Health_app.pptx) — Approach, Design, and Solution.




Health Information System
Overview
The Health Information System is a web application built with Python (Flask), MySQL, and Tailwind CSS. It is designed to manage health programs, register clients, and allow client enrollment and searches. The system provides a dashboard for managing health programs, client details, and interactions within the application.

Features
Client Registration: Allows adding new clients with basic details (name, age, gender, email).

Health Program Creation: Users can create health programs, providing a name and description.

Client Enrollment: Clients can be enrolled into health programs.

Client Search: Allows searching for clients by name, displaying their details and enrolled programs.

Client Profile: Displays detailed information about a client, including their enrolled programs.

Technologies Used
Backend: Python, Flask

Database: MySQL

Frontend: HTML, CSS, Tailwind CSS

Others: JavaScript for dynamic interactions

Installation
Prerequisites
Python 3.x

MySQL

Flask

Tailwind CSS (through CDN)

Steps to run the project locally
Clone this repository:

bash
Copy
Edit
git clone https://github.com/chegeMP/health__system.git
cd health__system
Install required Python dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up your MySQL database with the following structure:

Create a database for the system.

Set up the necessary tables for clients and health programs.

Configure database connection in the config.py file:

python
Copy
Edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/health_system'
Run the Flask application:

bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your browser to access the Health Information System.

Usage
Once the system is running, users can:

Register new clients.

Create new health programs.

Enroll clients into programs.

Search for clients by name.

View and manage client profiles.




