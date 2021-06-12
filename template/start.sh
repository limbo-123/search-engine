#This shell script will create and start Virtualenv for the Python, Once used make sure to move to Github vault or remove it.

#!/bin/bash
echo "Starting VirtualEnv for LinuxCLI search app"
source ./start/bin/activate
echo "Collecting All Static Files JS/CSS/AI Algos and files"
python3 manage.py collectstatic --no-input
echo "Creating Database And Tables"
python3 manage.py makemigrations
python3 manage.py migrate
echo "Running Dev Server"
python3 manage.py runserver 0.0.0.0:8080