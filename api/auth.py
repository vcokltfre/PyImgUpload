import hmac
import os
from flask import request

def authenticate(req: request):
    return hmac.compare_digest(req.headers.get("X-Api-Token", default=""), os.environ["TOKEN"])
