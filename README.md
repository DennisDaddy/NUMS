# StackOverflow-Lite
[![Build Status](https://travis-ci.com/DennisDaddy/MyDiary.svg?branch=challenge3)](https://travis-ci.com/DennisDaddy/MyDiary)

[![Maintainability](https://api.codeclimate.com/v1/badges/1aa0531c0fafdbfc3e8a/maintainability)](https://codeclimate.com/github/DennisDaddy/NUMS/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1aa0531c0fafdbfc3e8a/test_coverage)](https://codeclimate.com/github/DennisDaddy/NUMS/test_coverage)



StackOverflow-lite​ is a platform where people can ask questions and provide responses.


## How to use or contribute to this project
Follow the steps below if you're interested in contributing or using this API.
All the data is stored in the database, make sure you have installed PostgreSQL before getting started.

This API is built on the top of Flask python web framework.

### Heroku link
This is the link... https://gully.herokuapp.com/api/v1

### Setting up the environment

1. Install PostgreSQL.

2. Clone the repository.

```sh
$ git clone https://github.com/DennisDaddy/Nums.git
```

3. Access the cloned application directory.

```sh
$ cd Nums
```


4. Create the virtual environment and install dependencies(These are required Python, pip and virtual environment).

```sh
$ virtualenv venv
```

5. Activate the virtual environment [Linux].

```sh
$ source  venv/bin/activate
```


6. Install dependencies using pip.

```sh
$ pip install -r requirements.txt
```



### Running the API

To run the tests, use `nosetests` or any other test runner of your choice with the name of the test file at the end.

```sh
$ nosetests -v
```

Then run the app

```sh
$ python app.py
```

### API Endpoints

**`GET /api/v1`** *Root endpoint*

**`POST /api/v1/auth/register`** *User registration*

**`POST /api/v1/auth/login`** *User login*

**`POST /api/v1/auth/logout`** *User logout*

**`GET /api/v1/account`** *Get user account details*

**`GET /api/v1/questions`** *Get all the questions*

**`GET /api/v1/questions/<question_id>`** *Get single question*

**`POST /api/v1/questions`** *Create new question*

**`PUT /api/v1/questions/<question_id>`** *Update question details*

**`DELETE /api/v1/questions/<question_id>`** *Delete question*

**`GET /api/v1/answers`** *Get all the answers*

**`GET /api/v1/answers/<answer_id>`** *Get single answer*

**`POST /api/v1/answers`** *Create new answer*

**`PUT /api/v1/answers/<answer_id>`** *Update answer details*

**`DELETE /api/v1/answers/<answer_id>`** *Delete answer*

**`GET /api/v1/comments`** *Get all the comments*

**`GET /api/v1/comments/<comment_id>`** *Get single comment*

**`POST /api/v1/comments`** *Create new comment*

**`PUT /api/v1/comments/<comment_id>`** *Update comment details*

**`DELETE /api/v1/comments/<comment_id>`** *Delete comment*
