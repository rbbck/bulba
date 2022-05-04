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
- [ViaCep](https://viacep.com.br/): Location consulting

## Features

- [x] API REST/RESTFULL
- [x] Relational Database with SQLAlchemy
- [x] User class with Name, Surname, Nationality, CPF (Brazilian individual taxpayer registry identification), CEP (Brazilian Postal Addressing Code), State, City, Address, E-mail and Phone fields
- [x] Use a framework for front-end (Chose Bootstrap)
- [x] All fields are required and validated
- [x] Disallow creation of users with same CPF
- [x] [Viacep webservice integration](https://viacep.com.br/) for filling location fields dinamically
- [x] A page for each CRUD function (Though all of them are available on the Dashboard as well)
- [ ] Turn nationality into [SelectField](https://wtforms.readthedocs.io/en/2.3.x/fields/#wtforms.fields.SelectField) 
- [ ] Better CPF validation
- [ ] Better e-mail validation
- [ ] SPA (Single Page Application)
- [x] Docker container
- [ ] Test with [SQLMap](https://github.com/sqlmapproject/sqlmap)

## Recommended reading
- https://flask.palletsprojects.com/en/2.1.x/
- https://flask-login.readthedocs.io/en/latest/
- https://docs.sqlalchemy.org/en/14/
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/
- https://flask-wtf.readthedocs.io/en/1.0.x/
- https://wtforms.readthedocs.io/en/3.0.x/
- https://werkzeug.palletsprojects.com/en/2.1.x/
- https://getbootstrap.com/docs/4.6/getting-started/introduction/
- https://github.com/RobinHerbots/Inputmask#readme
- https://viacep.com.br/
- https://medium.com/@brunoeleodoro96/mitiga%C3%A7%C3%A3o-de-ataques-sql-injection-em-flask-python-b2e433e31e49 (in Portuguese)

## Installation
You can use Docker Compose

- `docker-compose build`

OR

_The commands here are for Linux, if you're running other OS, I'd recommend using Docker Compose or searching for your specific context_

- Activate the virtual environment `. venv/bin/activate`
- Install the requirements `pip install -r requirements.txt`

## Usage
- `docker-compose up -d`

OR

- `python run.py runserver`

Then

Go to your [localhost:5000](localhost:5000)
