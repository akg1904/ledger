from flask_restful import Api
from src.resource.health_check import HealthCheck
from src.resource.main_resource import RegisterResource, LoginResource, UserResource, UserDetailResource


def set_api(api: Api):
    api.add_resource(HealthCheck, '/health-check')
    api.add_resource(RegisterResource, '/register')
    api.add_resource(LoginResource, '/login-user')
    api.add_resource(UserResource, '/users')
    api.add_resource(UserDetailResource, '/user/<string:emp_id>')
