from flask_restful import Api
from src.resource.health_check import HealthCheck
from src.resource.main_resource import LoginResource


def set_api(api: Api):
    api.add_resource(HealthCheck, '/health-check')
    api.add_resource(LoginResource, '/login')
    # api.add_resource(LogoutResource, '/logout')
    # api.add_resource(Registration, '/registration')
    # api.add_resource(UserResource, '/user')
    # api.add_resource(UserDetailResource, '/user/<int:user_id>')
