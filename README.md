# Teacher Portal

A Django-based web application that allows teachers to:

✅ Register and login as a Teacher
✅ Add, edit, and delete student records  
✅ Each teacher has their own set of student records  
✅ Clean, modern UI with HTML, CSS, and JavaScript

---

## Features

- **Teacher Registration & Login**:  
  Teachers can register and login to access their portal.

- **Student Management**:  
  - View student list (name, subject, marks)  
  - Add new students  
  - Edit and delete existing students  
  - If a student with the same name and subject exists, marks are updated automatically.

- **Per-Teacher Data Isolation**:  
  Each teacher only sees and manages their own students.

- **Clean UI**:  
  Styled using vanilla CSS for a clean, user-friendly experience.

---

## Installation & Setup
**Presequits :**

- Python: The core language for Django.
- pip: Python's package installer, usually comes bundled with Python.
- Git: Required to clone the project repository from GitHub.
- Terminal or Command Prompt: To execute the commands provided in the setup guide.

**1. Open your Terminal**
Create a Project Folder and navigate into it
```bash
mkdir Python_project
cd Python_project
```
**2. Clone the repository**  
```bash
git clone https://github.com/SatsNik/Teacher_portal.git
cd Teacher_portal
```
**3. Creating .env file**

create a .env file in root direrctory(at manage.py file level)

**4. Generating Secret Key(if not provided in Readme file)**
Note : In Django, Secret key is a key to access the applicaion, for testing purposes or for demo projects -> it can be shared, but for production purposes -> Secret Key should never be shared(Highly Recommended).
```bash
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
This command will generate a long string(a Secret Key), copy it.

**5. Adding secret Key into .env file**

DJANGO_SECRET_KEY = 'YOUR_GENERATED_DJANGO_SECRET_KEY_HERE'

**6. Install Dependencies**
```bash
pip install -r requirements.txt
```

**7. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**8. Run the project locally**
```bash
python manage.py runserver
```
It will provide a local URL for the application.
