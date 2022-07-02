from functools import wraps


def token_required(name: str, age: int, print_start: bool):
    def login_required(func):

        @wraps(func)
        def verification_wrapper(*args, **kwargs):
            print(name, age)
            if print_start:
                print('start 1')
            func(*args, **kwargs)
            print('end 1')

        return verification_wrapper
    return login_required


@token_required(name="pramod", age=35, print_start=False)
def get_api(val1, val2):
    print(f'{val1}! {val2}')


get_api('hello', 'world')

