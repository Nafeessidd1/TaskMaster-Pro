# django-todo-app
This is a Django-based web application for managing todos. The app allows users to register, log in, and manage their personal todo lists. It includes features such as adding, updating, and deleting todos, along with user authentication to ensure that each user's data is private and secure.
## Features

- User registration and authentication (login/logout)
- Add new todos
- Mark todos as complete/incomplete
- Delete todos
- Responsive design with Bootstrap

## Tech Stack

- Django
- Bootstrap 4
- SQLite (default, can be changed to other databases)
- HTML, CSS, JavaScript

![TODO](https://github.com/Nafeessidd1/django-todo-app/blob/main/staticfiles/home1.png))
![SIGNUP](https://github.com/Nafeessidd1/django-todo-app/blob/main/staticfiles/signup.png))
![LOGIN](https://github.com/Nafeessidd1/django-todo-app/blob/main/staticfiles/login1.png))

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todoapp.git
    cd todoapp
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional, for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to view the application.

## Usage

1. **Register**: Create a new account by providing a username, email, and password.
2. **Login**: Log in to your account.
3. **Add Todos**: Use the form to add new todos.
4. **Mark as Complete**: Check the checkbox next to a todo to mark it as complete.
5. **Delete Todos**: Click the trash icon next to a todo to delete it.
6. **Logout**: Log out from your account when done.

## Project Structure


Cheers and Happy Coding :)
