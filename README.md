# mysite  August 8 2022
This is my latest personal website created with Flask 2.1.3 and hosted on PythonAnywhere.

## [Live site]('https://zyambo.pythonanywhere.com')
## Technologies used
- Python 3.9
- Flask 2.1.3
- HTML
- CSS
- JavaScript

## Hosting
- [PythonAnywhere](https://pythonanywhere.com)

### repository - mysite
### working directory - zyambo
### application entry point - app.py

# Main functions and routes
### zyambo/app.py
- def not_found(error): decorated function that handles 404 error.
- def unauthorized(error): decorated function that handles 401 error.

## Project layout
| Directory and Path | Description |
|---------------------------------------|-----------------|
|zyambo/| package containing all the applications code and files |
|zyambo/views/| a package containing app views|
|zyambo/templates/| a directory containing HTML files|
|zyambo/static/| a directory containing static file folders|
|zyambo/static/css| a directory containing stylesheet(css) files|
|zyambo/static/img| a directory containing images |
|zyambo/static/js| a directory containing JavaScript files|
|zyambo/tests| directory with test modules|

## Blueprints and views functions
## Blueprint
This organizes a group of related views and other code. Views are registered with this blue print rather than directly with an application.

### zyambo/views/__init__.py
- app_views = Blueprint("app_views", __name__, url_prefix="/")
## views
|module | description| 
|---------------------|-----------------|
| about.py |responds to 'GET' requests sent to the "zyambo/about" route |
| contact.py |responds to 'GET, POST' requests sent to the "zyambo/contact" route |
| index.py |responds to 'GET' requests sent to the home route|
| project.py |responds to 'GET, POST' requests sent to the "zyambo/about" route |

## Running project on local machine
- clone this repo
$ git clone git@github.com:sangwani-coder/mysite.git
$ cd mysite

## Install requirements
$ pip3 install -r requirements.txt

## Starting project
open zyambo/app.py and uncomment the following code:
# if __name__ == "__main__":
#     app.jinja_env.auto_reload = True
#     app.config['TEMPLATES_AUTO_RELOAD'] = True
#     app.run(debug=True, host='0.0.0.0')

* then make sure you're inside the root of the project directory (mysite) and run:
$ python3 -m zyambo.app

Author: Peter S. Zyambo <Twitter: @peter_zyambo>