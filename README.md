# Personal Assistant

It assists you in organizing the phone book, creating notes, and more.

## Installation

**Note:** The Docker command is optional since the project can work with
`SQLite` when environment variables for `PostgreSQL` are not defined.

```bash
$ git clone https://github.com/BIN0VA/Personal-Assistant.git
$ cd Personal-Assistant
$ docker compose up -d
$ poetry shell
$ poetry install
$ cd personal_assistant
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Usage

```bash
$ docker compose up -d
$ poetry shell
$ cd personal_assistant
$ python manage.py runserver
```

Go to http://localhost:8000.
