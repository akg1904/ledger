from flask_restful import Api
from src.resource.health_check import HealthCheck
from src.resource.login import LoginResource

def set_api(api: Api):
    api.add_resource(HealthCheck, '/health-check')
    api.add_resource(LoginResource, '/login')