Language Translation Tool  - project Documentation
Setup:
•	Ensure python 3.X and pip installed.
•	Create a virtual environment:
•	Open command prompt and fallow the commands:
py -m venv venv_name
•	activate the virtual environment:
venv_name\Scripts\activate.bat
Packages required:
•	make sure the Django, googletrans and pytesseract is required.
pip install django googletrans
Database migrations:
•	Apply migrations :
py manage.py makemigrations
then 
py manage.py migrate
Run the project:
•	Start the development server:
py manage.py runserver
•	Access the app at:
http://127.0.0.1:8000/
note:
	this app supports language translation for various functionalities.






