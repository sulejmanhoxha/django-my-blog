# README
This repository contains the code for my personal blog website built with Django and Tailwind CSS.

## Installation
### 1. Clone the repository
Clone this repository by running the following command in your terminal:
```bash
git clone git@github.com:sulejmanhoxha/django-my-blog.git
```

### 2. Create virtual environment
Make sure you have Python 3.10.5 and pip 23.0.1 installed on your computer. Then, create a virtual environment by running the following command:

 **All the following commands are for Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install required packages
Install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

### 4. Run the server
Finally, run the server with the following command:

```bash
python3 manage.py runserver
```
You should now be able to access the blog website at http://localhost:8000/.
### 5. *Optional* - Install Tailwind CSS

This project uses Tailwind CSS for styling and it should run without having it installed. If you want to modify the project's look you need to install Tailwind CSS. To do that open up a new terminal window or tab and run the following commands:

```bash
npm install
npm run watch
```

### Potential problems
If you have problems with the database run the following commands:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata database_data.json
```

## Project Structure
Here's a brief overview of the project structure:

```
./blog/    # Contains the Django app for the blog
./base/    # Contains the Django project settings
./static/  # Contains static files (CSS, JS, images, etc.)
./templates/ # Contains the HTML templates
./db.sqlite3  # SQLite database file
./manage.py   # Django management script
./README.md   # This file
./requirements.txt  # Required Python packages
./tailwind.config.js # Tailwind CSS configuration file
./package.json # Contains project dependencies for Node.js
./package-lock.json # Lock file for project dependencies for Node.js
```

Some screenshots:
![alt text](https://github.com/sulejmanhoxha/django-my-blog/blob/master/screenshot1.png)
![alt text](https://github.com/sulejmanhoxha/django-my-blog/blob/master/screenshot2.png)
![alt text](https://github.com/sulejmanhoxha/django-my-blog/blob/master/screenshot3.png)

## Contributing
If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.
