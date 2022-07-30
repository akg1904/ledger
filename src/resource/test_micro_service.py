import json
import uuid
from datetime import timedelta

import requests
from flask import request
from requests import Response

from src.resource.base import BaseResource
from src.shared.decorators.auth import login_validate


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





