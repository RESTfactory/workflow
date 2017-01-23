# Workflow
Workflow is a REST API intended to be used as a general purpose workflow system.

## Installation
1. Clone this repository
	> git clone https://github.com/RESTfactory/workflow.git

2. get into the project folder
	> cd workflow

3. Install the required packages
	> pip install -r requirements.txt

4. get into main django folder
	> cd workflow

5. Rename workflow/settings_secret.py.dist to workflow/settings_secret.py
  > mv workflow/settings_secret.py.dist workflow/settings_secret.py

6. Migrate
	> python manage.py makemigrations && python manage.py migrate

7. Create a superuser
	> python manage.py createsuperuser

8. run and visit the app in http://localhost:8000/admin with your username and password
	> python manage.py runserver

## Models
The project provides the following models:
- **ContactInfo**: Provides info about the person, manager, client, etc. we need to contact in a task.
- **Status**: It's the status of the task, intended to be used through a step
- **Step** : The step that a task is on, or the possible steps that are allowed in a workflow
- **Workflow**: The flow that is needed to be done, it has a name, a description and a list with allowed steps
- **Task**: Is an *instance* of a workflow, its intended to be more specific than a workflow
- **TaskInstance**: is an snapshot of a task, created automatically everytime a task is saved, it's intended to be used as a audit model
- **TaskHistory**: is a collection of TaskInstance, asociated to a Task. Allows to the Django Admin to audit all the states of a task. It's created the first time a task is saved, and auto associates the Task with all it's TaskInstance.
- **Comment**: is a text associated to a task. Allow to specify actions or info about whats happening on a task.
