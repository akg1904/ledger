from flask import Flask
from flask_restful import Resource, Api

from src import routes

app = Flask(__name__)
api = Api(app)

routes.set_api(api)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
