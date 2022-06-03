from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy.orm import sessionmaker

from src.database.db.postgresql import PostgresDB
# from src import routes
from src.resource import login

app = Flask(__name__)
api = Api(app)

app.config['DB_INSTANCE'] = PostgresDB().get_connection()
app.config['DB_SESSION'] = sessionmaker(bind=app.config['DB_INSTANCE'])

# routes.set_api(api)
api.add_resource(login.LoginResource, '/login')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
