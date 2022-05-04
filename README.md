# bulba
User management app made with Python, HTML, CSS and Js

[![Python 3.10.4](https://img.shields.io/badge/python-3.10.4-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-WTFPL-red.svg)](https://raw.githubusercontent.com/VzrvU43mB4mxiT/bulba/main/LICENSE)

## Used in development
- Flask: Python micro framework for front-end web development
- Flask-Login: Provides user session management for Flask
- SQLAlchemy: Python SQL toolkit ORM for database stuff
- Flask-SQLAlchemy: SQLAlchemy Flask integration
- Flask-WTF: WTForms Flask integration
- WTForms: Forms validation and rendering
- Werkzeug: Security related validations
- Bootstrap: Frontend toolkit for styling purposes
- [Inputmask](https://github.com/RobinHerbots/Inputmask): For masking the form inputs and rendering the data with the correct format

## Installation
You can use Docker Compose

	- docker-compose build

OR

_The commands here are for Linux, if you're running other OS, I recommend using Docker Compose or searching for your specific context_

	Activate the venv
	`. venv/bin/activate`
	`pip install -r requirements.txt`

## Usage
	`docker-compose up -d`

OR

	`python run.py runserver`

Then

	Go to your localhost:5000
