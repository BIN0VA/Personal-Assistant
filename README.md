# Personal Assistant

It assists you in organizing the phone book, creating notes, and more.

## Development

```bash
$ git clone git@github.com:BIN0VA/Personal-Assistant.git
$ cd Personal-Assistant
$ poetry export --without-hashes --format=requirements.txt > requirements.txt
$ django-admin startproject personal_assistant
$ cd personal_assistant
$ python manage.py startapp pa_core
$ python manage.py startapp pa_user
$ python manage.py makemigrations
$ python manage.py collectstatic
```

## Deployment

```bash
$ git clone https://github.com/BIN0VA/Personal-Assistant.git
$ cd Personal-Assistant
$ poetry shell
$ poetry install
$ cd personal_assistant
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Usage

```bash
$ poetry shell
$ cd personal_assistant
$ python manage.py runserver
```

Go to http://localhost:8000.
