from flask import Flask, Response
from flask_pymongo import PyMongo

from app.api.vendor import vendor_endpoint
from app.api.content import content_endpoint

app = Flask(__name__)
app.register_blueprint(vendor_endpoint, url_prefix="/api/v1/vendor")
app.register_blueprint(content_endpoint, url_prefix="/api/v1/content")

app.config["MONGO_URI"] = "mongodb://localhost:27017/hair"


@app.route("/ping", methods=["GET"])
def pong():
    return Response("pong", status=200, mimetype="text/plain")


mongo = PyMongo(app)
