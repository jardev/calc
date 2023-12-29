# Project Overview

A simple Django Ninja based API to evaluate mathematical expressions. Provides the following URLs:
* `/api/docs` - API documentation + sandbox
* `/api/calc` - the API endpoint

Usage examples:
* http://127.0.0.1:8000/api/calc?expression=2%2B2
  ```
  {"result": 4}
  ```
* http://127.0.0.1:8000/api/calc?expression=10%2A2%2B100%2F5
  ```
  {"result": 40.0}
  ```

You can play with the API via http://127.0.0.1:8000/api/docs

# Installation

1. Install Python
2. Install [poetry](https://python-poetry.org/)
3. `$ poetry install`

# Run locally

* `$ poetry run python manage.py runserver`
