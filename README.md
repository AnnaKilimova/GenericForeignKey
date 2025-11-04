# GenericForeignKey
This project uses **PostgreSQL** as its database backend.

## ⚙️ Installation
### 1. Clone the repository
```bash
git clone git@github.com:AnnaKilimova/GenericForeignKey.git
```
### 2. Navigate to the project folder:
```bash
cd generic_foreign_key
```
### 3. Create and activate a virtual environment
#### For MacOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate    
```  
#### For Windows:
```bash
venv\Scripts\activate    
```
### 4. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt    
```
This installs all required packages listed in requirements.txt, ensuring your environment matches the project dependencies.

### 5. Install PostgreSQL
Make sure PostgreSQL is installed and running locally:
- macOS: `brew install postgresql`
- Ubuntu: `sudo apt install postgresql`
- Windows: Download from [https://www.postgresql.org/download/](https://www.postgresql.org/download/)

### 6. Create a database and user
After installing PostgreSQL, create a database and a user for the project:
```bash
psql -U postgres
CREATE DATABASE myproject_db;
CREATE USER myproject_user WITH PASSWORD 'mypassword';
ALTER ROLE myproject_user SET client_encoding TO 'utf8';
ALTER ROLE myproject_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE myproject_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject_db TO myproject_user;
\q
```
### 7. Configure your .env file
Create a .env file in the project root and add your database configuration:
<br>⚠️ Do NOT commit this file to GitHub. Use .env.example as a template.
```bash
SECRET_KEY=secret_key
DEBUG=True
DATABASE_NAME=myproject_db
DATABASE_USER=myproject_user
DATABASE_PASSWORD=mypassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 8. Apply migrations:
```bash
python manage.py migrate
```
## 🧩 Task Description
Create an ActionLog model to store information about actions (logs). Each log must contain:

- The action_type field (for example, ‘create’, “update”, ‘delete’).
- A timestamp field (date and time of the action).
- A user field (a reference to the user who performed the action, using ForeignKey on auth.User).
- Fields for GenericForeignKey so that the log can refer to any object (e.g., post, comment, or user).
- Create GenericRelation for all models (if possible, implement functionality that will track which models have relationships with GenericForeignKey).

Add at least 7 test records with dynamic relationships to at least 3 models. You can fill in the data in any way that is convenient for you.


### 🧪 Running Tests
```bash
python manage.py test
```
Tests cover:
- Verify that logs can be successfully created and linked to various object types (Post, Comment, Profile).
- Ensure that objects can access their logs via reverse GenericRelation.
- Test that a delete action log is created correctly and associated with the right user and object.
### 🙋‍♂️ Create superuser
```bash
python manage.py createsuperuser
```
### 🚀 Running the Application
After tests pass, start the server:
```bash
python manage.py runserver
```
The project will be available at:
```bash
👉 http://127.0.0.1:8000/
```
Available route:
- [/admin/](http://127.0.0.1:8000/admin/) - admin panel

Stop the server:
```bash
^C
```