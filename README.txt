To-Do List App:

    This Django-based To-Do List app allows users to manage tasks efficiently. 
    Follow the steps below to set up and run the application.

Prerequisites:

    1. Ensure you have Python installed on your system. You can download it from python.org.
    
    2. Install Django and Django Rest Framework using the following commands.
        a. pip install django
        b. pip install djangorestframework

Getting Started:

    1. Download Code or Clone.
        a. Download or clone the code repository from github to your local machine.
        b. Use the following command in the terminal to clone github repo.
            i. git clone <repository_url>.
           ii. Use the github repository location url in place of <repository_url>. 

    2. Navigate to Project Directory:
        a. Open a terminal or command prompt and navigate to the directory,
           where you downloaded the ToDoList App code.
    
    3. Apply Migrations:
        a. Run the following commands to apply the database migrations:        
             i. python manage.py makemigrations.
            ii. python manage.py migrate.

    4.Create Superuser (Optional):
        a. Create a superuser to access the Django Admin interface using following command:
            i. python manage.py createsuperuser.
    NOTE: The superuser creation is optional or else use the provided superuser credentials.

    5. Run Development Server:
        a. Start the Django development server using following command:
            i. python manage.py runserver

    6. Access Admin Interface:
        a. Open a web browser and go to https://punitlanjewar.pythonanywhere.com/admin/. 
        b. Log in with the superuser credentials.                 

    7. Create Todo Items:
        a. In the Django Admin interface, you can create, update, and delete To-Do List items.

    8. Access API Endpoints:
        a. Explore the To-Do List API endpoints:
            i. Create: https://punitlanjewar.pythonanywhere.com/create-item
           ii. Read One: https://punitlanjewar.pythonanywhere.com/read-item/{item_id}
          iii. Read All: https://punitlanjewar.pythonanywhere.com/list-items
           iv. Update: https://punitlanjewar.pythonanywhere.com/update-item/{item_id}
            v. Delete: https://punitlanjewar.pythonanywhere.com/delete-item/{item_id}        
        b. To generate token for authentication:
            i. https://punitlanjewar.pythonanywhere.com/api-token-auth

    9. Stop the Server:
        a. Press Ctrl + C in the terminal to stop the Django development server.        