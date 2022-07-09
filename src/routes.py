from flask_restful import Api

from src.resource.admin.item import ItemResource, ItemDetailResource
from src.resource.admin.rate import RateResource, RateDetailResource
from src.resource.admin.stock import StockResource, StockDetailResource
from src.resource.auth.login import LoginResource
from src.resource.auth.register_resource import RegisterResource
from src.resource.auth.user_resource import UserResource, UserDetailResource
from src.resource.health_check import HealthCheck
from src.resource.test_micro_service import Test


def set_api(api: Api):
    api.add_resource(HealthCheck, '/health-check')
    api.add_resource(RegisterResource, '/register')
    api.add_resource(LoginResource, '/login-user')
    api.add_resource(UserResource, '/users')
    api.add_resource(UserDetailResource, '/user/<string:emp_id>')
    api.add_resource(ItemResource, '/item')
    api.add_resource(ItemDetailResource, '/item/<string:code>')
    api.add_resource(RateResource, '/item/<string:item_code>/rate')
    api.add_resource(RateDetailResource, '/item/<string:item_code>/rate/<string:rate_id>')
    api.add_resource(StockResource, '/item/<string:item_code>/rate/<string:rate_id>/stock')
    api.add_resource(StockDetailResource, '/item/<string:item_code>/rate/<string:rate_id>/stock/<string:id>')
    api.add_resource(Test, '/test')



