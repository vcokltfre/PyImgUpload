import os
from flask import request

def authenticate(req: request):
    if "X-Api-Token" not in req.headers:
        return False

    if not req.headers["X-Api-Token"] == os.environ["TOKEN"]:
        return False

    return True