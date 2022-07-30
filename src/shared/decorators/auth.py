import json
from datetime import timedelta
from functools import wraps

from flask import request


def login_validate(func):

    @wraps(func)
    def login_wrapper(self, *args, **kwargs):

        if not request.headers.get('TOKEN', False):
            return {'message': "Token missing"}

        token = request.headers.get('TOKEN')
        token_key = "ledger_" + token

        if self.message_bus.redis.get(token_key):
            data = self.message_bus.redis.get(token_key)
            self.message_bus.redis.setex(token_key, timedelta(minutes=int(60)), data)
            return func(*args, **kwargs)

        return {"message": "invalid token"}, 401
    return login_wrapper


# def token_required(name: str, age: int, print_start: bool):
#     def login_required(func):
#     #
#         @wraps(func)
#         def verification_wrapper(*args, **kwargs):
#             print(name, age)
#             if print_start:
#                 print('start 1')
#             func(*args, **kwargs)
#             print('end 1')
#     #
#         return verification_wrapper
#     return login_required
#
#
# @token_required(name="pramod", age=35, print_start=False)
# def get_api(val1, val2):
#     print(f'{val1}! {val2}')
#
#
# get_api('hello', 'world')
#
# get_api(val1='hello', val2='world')
#
# get_api('hello', val2='world')
