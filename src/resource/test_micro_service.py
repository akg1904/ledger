import json
import uuid
from datetime import timedelta

import requests
from flask import request
from requests import Response

from src.resource.base import BaseResource


def login_validate(func):

    def login_wrapper(self):
        token = request.headers.get('TOKEN')
        token_key = "ledger_" + token

        if self.message_bus.redis.get(token_key):
            data = self.message_bus.redis.get(token_key)

            self.message_bus.redis.setex(token_key, timedelta(seconds=int(20)), data)
            return {"data": json.loads(data), "message": "data found"}

        return {"message": "invalid token"}, 401
    return login_wrapper


class Test(BaseResource):

    def get(self):
        res: Response = requests.get('http://localhost:5002/health')
        print(res.status_code, res.json())
        if res.status_code == 200:
            return res.json()

    def post(self):
        data = request.get_json()

        token = uuid.uuid4().hex
        token_key = "ledger_" + token

        self.message_bus.redis.setex(token_key, timedelta(seconds=int(20)), json.dumps(data))

        return {"token": token, "message": "token generated"}

    @login_validate
    def put(self):
        token = request.headers.get('TOKEN')
        token_key = "ledger_" + token

        # if self.message_bus.redis.get(token_key):
        #     data = self.message_bus.redis.get(token_key)
        #
        #     self.message_bus.redis.setex(token_key, timedelta(seconds=int(20)), data)
        #
        #     return {"data": json.loads(data), "message": "data found"}
        #
        #
        # return {"message": "invalid token"}, 401





