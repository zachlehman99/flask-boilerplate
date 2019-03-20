1. mkdir
2. git init
3. gitignore file take from flaskr project
4. setup file take from the flaskr project
    -> Add pytest and coverage
    -> extras_require={
        'test':[
            'pytest',
            'coverage',
            ]
      },
5. virtual environment set it up.
    -> python3 -m venv venv
6. then source it...run in...use which python to check if the venv will work
7. pip install -e .
8. which flask....tells you where flask is
9. pip install -e '.[test]'    You get pytest and coverage
10. echo $FLASK_APP
11. echo $FLASK_ENV
12. export FLASK_APP=flask_boilerplate
13. export FLASK_ENV=development
14. mkdir flask_boilerplate
    in the flask_boilerplate __init__.py
15. from flask import Flask

    def create_app():
      app = Flask(__name__)

      @app.route('/')
      def index():
          return 'Hello, World!'

      return app
