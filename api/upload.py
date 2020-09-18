import os
from random import choice
from string import ascii_letters
from pathlib import Path
from flask import request, Response

from .auth import authenticate


class Uploader:
    def __init__(self):
        pass

    def random_id(self):
        return ''.join([choice(ascii_letters) for i in range(16)])

    def new_filename(self, extension):
        name = self.random_id()

        while Path(f"{name}.{extension}").exists():
            name = self.random_id()

        return name

    def upload(self, req: request):
        # Error handling
        if not authenticate(req):
            return Response("Invalid authentication", 403)

        if not 'file' in req.files:
            return Response("No file provided.", 400)

        file = req.files['file']

        if not file.filename:
            return Response("No file provided.", 400)

        # Main uploader code
        name_parts = file.filename.split(".")
        extension = name_parts.pop()
        name = self.new_filename(extension)

        fp = f"static/{name}.{extension}"

        file.save(fp)
        return Response(f"http://{os.environ['HOST']}/{fp}", 200)