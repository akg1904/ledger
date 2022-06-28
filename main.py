from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Health(Resource):

    def get(self):
        return {"msg": "signal"}


api.add_resource(Health, '/health')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
