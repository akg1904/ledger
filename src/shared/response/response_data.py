

def response_payload(data=None, message="Operation Successful", code=2000, status=True):
    return {
        "data": data,
        "message": message,
        "code": code,
        "status": status
    }
