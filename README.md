# StackOverflow-Lite
[![Build Status](https://travis-ci.com/DennisDaddy/NUMS.svg?branch=master)](https://travis-ci.com/DennisDaddy/NUMS)



StackOverflow-lite​ is a platform where people can ask questions and provide responses.


## How to use or contribute to this project
Follow the steps below if you're interested in contributing or using this API.
All the data is stored in the database, make sure you have installed PostgreSQL before getting started.

This API is built on the top of Flask python web framework.



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
