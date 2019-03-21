from flask import Flask, request, make_response, render_template


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
        # print(request.)
        # print('=' * 20)
        return render_template('index.html')

    @app.route('/hello')
    def hello():

        # for key, value in request.args.items():
        #     print(f"{key}: {value}")

        # print(request.args)
        # print(type(request.args))
        name = request.args.get('name', 'World')
        return render_template('hello.html', name=name)

    method_route_allows = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']

    @app.route('/method', methods=method_route_allows)
    def method_route():
        return render_template('method.html', allowed=method_route_allows, method=request.method)


    @app.route('/calculate', methods=['GET', 'POST'])
    def calculate():
        if request.method == 'GET':
            return render_template('calculate.html', action='Add')
        elif request.method == 'POST':
            x = float(request.form['x'])
            y = float(request.form['y'])
            action = request.form['action']

            if action == 'Add':
                result = x + y
            elif action == 'Subtract':
                result = x - y
            elif action == 'Multiply':
                result = x * y
            elif action == 'Divide':
                result = x / y

        return render_template('calculate.html', result=result, x=x, y=y)

    @app.route('/number/<int:num>')
    def number_route(num):
        return f"Number: {num}"

    # @app.route('/method', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
    # def method_route():
    #     if request.method == 'GET':
    #         return f"HTTP Method: GET"
    #     elif request.method == 'POST':
    #         return f"HTTP Method: POST"
    #     elif request.method == 'PATCH':
    #         return f"HTTP Method: PATCH"
    #     elif request.method == 'PUT':
    #         return f"HTTP Method: PUT"
    #     elif request.method == 'DELETE':
    #         return f"HTTP Method: DELETE"
    #     else:
    #         return 'You done did break it'

    @app.route('/status')
    def status_route():
        code = request.args.get('c', 200)
        response = make_response(f"status: {code}", code)

        return response



    @app.route('/mystuff')
    def mystuff():
        return """
        <h1 style="color:blue; font-size:50px; text-align: center;">Please Read This</h1>
        <h2 style="text-align: center;">Then This One</h2>
        <script> alert('This is just messing around with stuff')</script>
        """


    return app
