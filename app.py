from flask import Flask, request

from api.upload import Uploader

app = Flask(__name__)
uploader = Uploader()

@app.route("/api/upload", methods = ["POST"])
def upload():
    return uploader.upload(request)

if __name__ == "__main__":
    app.run()