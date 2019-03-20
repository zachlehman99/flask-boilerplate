from flask import Flask, request


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        # print('=' * 20)
        # print(request.date)
        # print('=' * 20)
        return 'This is a flask-boilerplate project, not to be used in production'

    @app.route('/hello')
    def hello():

        for key, value in request.args.items():
            print(f"{key}: {value}")

        # print(request.args)
        # print(type(request.args))
        name = request.args.get('name', 'World')
        return f"Hello {name}!"

    @app.route('/number/<int:num>')
    def number_route(num):
        return f"Number: {num}"

    @app.route('/mystuff')
    def mystuff():
        return """
        <h1 style="color:blue; font-size:50px; text-align: center;">Please Read This</h1>
        <h2 style="text-align: center;">Then This One</h2>
        <script> alert('This is just messing around with stuff')</script>
        """


    return app
