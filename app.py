from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy.orm import sessionmaker

from src.database.db.postgresql import PostgresDB
from src.resource.health_check import HealthCheck
from src import routes


app = Flask(__name__)
api = Api(app)

app.config['DB_INSTANCE'] = PostgresDB().get_connection()
app.config['DB_SESSION'] = sessionmaker(bind=app.config['DB_INSTANCE'])

routes.set_api(api)


if __name__ == '__main__':
    app.run(debug=True)
