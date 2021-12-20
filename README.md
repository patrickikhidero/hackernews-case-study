# Hacker News Clone

This is a Django web application that retrieves data from Hacker News API and makes it easier to navigate the news items. It provides search and filter functionality and also enables clients, through three API endpoints, to create news items, modify and delete only the items they created and provide read-only access to news items generated from Hacker News API server. 


## Technologies 

The following technologies were used in this project:

- [HTML](https://html.com/)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Hacker News API](https://hackernews.api-docs.io/v0/overview/introduction)
- [SQLite3](https://www.sqlite.org/index.html)


## Requirements

Before starting, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

Kindly ensure that you are in the root directory before running the following commands.

## Create a virtual environment

    python3 -m venv env

## Activate the virtual environment

    . env/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Collect Static files

    python manage.py collectstatic

## Run Tests

    python manage.py test

## Fetch data from Hacker News API

    python manage.py shell < hn_api.py

## Start server
    Open another terminal window, activate the virtual environment and run the following command:

    . env/bin/activate && python manage.py runserver 8080


# Endpoints

The endpoints, expected payloads, and responses are described below.


## Get all news items 

### Request

`GET api/v1/news/`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8080/api/v1/news/

### Response

    {
        "message": "success",
        "data": {
            "news": [
                [
            {
                "id": "c21b9f5f-72dd-4db7-8581-f49fcbba9087",
                "title": "4nm Mac ‘M2’ chip to arrive in second of half of 2022, and ‘M2 Pro’ in 2023",
                "author": "retskrad",
                "type": "story",
                "url": "https://9to5mac.com/2021/12/20/m2-m2-pro-chips-rumor/",
                "text": "",
                "score": 2,
                "is_from_api": true
            },
            {
                "id": "6793f01c-1ea0-409e-af2b-13785414368d",
                "title": "A Food App Has Made Its First Delivery in Space",
                "author": "rustoo",
                "type": "story",
                "url": "https://theswaddle.com/a-food-app-has-made-its-first-delivery-in-space/",
                "text": "",
                "score": 2,
                "is_from_api": true
            }
            ]
        },
        "errors": null
    }

## Create a news item

### Request

`POST api/v1/add-news`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8080/api/v1/add-news

### Payload

    {
        "title": <String>,
        "author": <String>,
        "type": <String>
        "text": <String>
        "score": <Integer>
    }

### Response

    {
        "message": "success",
        "data": {
            "news": {
                "id": <UUID>,
                "title": <String>,
                "author": <String>,
                "type": <String>
                "url": <String>,
                "text": <String>
                "score": <Integer>,
                "is_from_api": <Boolean>
            }
        },
        "errors": null
    }


## Get a specific news item by its ID

### Request

`GET api/v1/news/<id>`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8080/api/v1/news/<id>

### Response

    {
        "message": "success",
        "data": {
            "news": {
                "id": <UUID>,
                "title": <String>,
                "author": <String>,
                "type": <String>
                "url": <String>,
                "text": <String>
                "score": <Integer>,
                "is_from_api": <Boolean>
            }
        },
        "errors": null
    }


## Update a news item

### Request

`PUT api/v1/news/<id>`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8080/api/v1/news/<id>

### Payload

    {
        "title": <String>,
        "author": <String>,
        "type": <String>
        "text": <String>
        "score": <Integer>
    }

### Response

    {
        "message": "success",
        "data": {
            "news": {
                "id": <UUID>,
                "title": <String>,
                "author": <String>,
                "type": <String>
                "url": <String>,
                "text": <String>
                "score": <Integer>,
                "is_from_api": <Boolean>
            }
        },
        "errors": null
    }


## Delete a news item

### Request

`DELETE api/v1/news/<id>` 

    curl -i -H 'Accept: application/json' http://127.0.0.1:8080/api/vi/news/<id>

### Response

    {
        "message": "success",
        "data": {
            "news": {}
        },
        "errors": null
    }
