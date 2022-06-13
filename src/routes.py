from flask_restful import Api

from src.resource.auth.login import LoginResource
from src.resource.auth.register_resource import RegisterResource
from src.resource.auth.user_resource import UserResource, UserDetailResource
from src.resource.health_check import HealthCheck


def set_api(api: Api):
    api.add_resource(HealthCheck, '/health-check')
    api.add_resource(RegisterResource, '/register')
    api.add_resource(LoginResource, '/login-user')
    api.add_resource(UserResource, '/users')
    api.add_resource(UserDetailResource, '/user/<string:emp_id>')
