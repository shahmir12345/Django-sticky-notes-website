# Sticky Notes Django Assignment Solution

This project is a complete solution for the Django Sticky Notes.

## Features
- User registration using `UserCreationForm`
- User login and logout using Django built-in authentication views
- Create, view, edit, and delete personal sticky notes
- Each note has a title, content, color, timestamps, and owner
- Login protection on all note pages
- Users can only access their own notes
- Base template with navigation bar and reusable layout

## Setup Instructions
1. Create a virtual environment {
   python -m venv .venv             <!-- -   Current Folder main venv banata hai   -->
}. 
 
2. Activate Virtual Environment {
   venv\Scripts\Activate
}

3. Install Django:
   ```bash
   pip install django
   ```
4. Go to the project folder and run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```
6. Open the browser and visit:
   - `http://127.0.0.1:8000/register/`
   - `http://127.0.0.1:8000/login/`
   - `http://127.0.0.1:8000/notes/`
   - `http://127.0.0.1:8000/notes/<id>/edit/`
   - `http://127.0.0.1:8000/notes/<id>/delete/`
   - `http://127.0.0.1:8000/notes/new/`
   - `http://127.0.0.1:8000/admin/notes/note/`        <!-- -   Admin bhi dekh sakta hai saaray notes ko    -->
 
## Optional Admin Access
To create an admin account:
```bash
python manage.py createsuperuser   #you can create also superuser who can run admin panel 
```
Then visit `/admin/`.

## Migrations 
To Tell the Dtabase, when you change model.py file uou can run Migration r Migrate commands to Detect any issue related to data
```bash
python manage.py makemigrations app_name
pyhton manage.py migrate app_name
``` 
## runserver
Then run main command to run server
```bash
python manage.py runserver (Define port if 8000 not works)
``` 

## Change Admin or superuser Password
to Change Superuser password
```bash
python manage.py changepassword username
``` 
