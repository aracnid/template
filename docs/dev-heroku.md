# How to Setup Flask and Deploy it to Heroku

## Setup Procedure

This procedure describes how to setup Flask and deploy it to Heroku. 

The project name, `TEMPLATE`, used in this procedure is a placehold and should be replaced. (Capitalization of `TEMPLATE` is only used for emphasis.)

### 1. Install Dependencies

Make sure the correct virtual environment is active.

```bash
$ pip install flask gunicorn
```

### 2. Create the base Flask app

Add the following code to `app.py`:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run()
```

### 3. Run the Flask app

```bash
$ python app.py
```

### 4. Verify that the app is running

Navigate your browser to `http://localhost:5000/`. The browser should display 'Hello, World!'.

### 4. Update the `requirements.txt` file

```bash
$ pip freeze > requirements.txt
```

### 5. Create a `Procfile`

Create a file named `Procfile` in the root directory of the project repository. Add the following line to the file:

```
web: gunicorn app:app --log-file -
```

### 6. Deploy the app to Heroku

Using the Heroku CLI, create a new Heroku app and deploy it.

```bash
$ heroku create TEMPLATE
$ git push heroku master
$ heroku open
```

## Workflow

N/A

## Directory Structure

The final directory structure looks like the following. Files and directories not related to testing are not shown.

```
TEMPLATE/              # project repository
├── TEMPLATE/          # main python package
│   ├── __init__.py    # python module package file
│   └── app.py         # main application program
└── Procfile           # Heroku process file
```
