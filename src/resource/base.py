from flask_restful import Resource

from src.bootstrap import main_bootstrap
from src.bootstrap.bus.message_bus import MessageBus


class BaseResource(Resource):
    message_bus: MessageBus = main_bootstrap.bootstrap()