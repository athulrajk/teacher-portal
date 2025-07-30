# teacher-portal
# 🧑‍🏫 Teacher Portal – Django + HTML/JS

A robust teacher portal built with Django (Python), HTML, CSS, and vanilla JavaScript. It includes login functionality and a dashboard to manage student records.

---

## 🚀 Features

- ✅ Secure Teacher Login
- ✅ Student Listing on Home Page
- ✅ Add New Student via Modal
- ✅ Edit and Delete Student Records
- ✅ Duplicate Detection (based on name + subject)
- ✅ Marks auto-update on duplicate entry
- ✅ Clean, responsive UI

---

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Database**: SQLite (default)

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone 
cd teacher-portal

2. Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Apply Migrations & Create Superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver


