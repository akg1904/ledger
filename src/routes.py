from flask_restful import Api

from src.resource.admin.item import ItemResource, ItemDetailResource
from src.resource.admin.rate import RateResource
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
    api.add_resource(ItemResource, '/item')
    api.add_resource(ItemDetailResource, '/item/<string:code>')
    api.add_resource(RateResource, '/rate')


