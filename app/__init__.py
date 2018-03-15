import os

from flask import Flask, Response, render_template
from flask_pymongo import PyMongo

from app.api.content import content_endpoint
from app.api.vendor import vendor_endpoint

frontend_dir = os.path.abspath("templates/")
static_dir = os.path.abspath("static/")
app = Flask(__name__, template_folder=frontend_dir, static_folder=static_dir)

app.register_blueprint(vendor_endpoint, url_prefix="/api/v1/vendor")
app.register_blueprint(content_endpoint, url_prefix="/api/v1/content")

app.config["MONGO_URI"] = "mongodb://localhost:27017/hair"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/ping", methods=["GET"])
def pong():
    return Response("pong", status=200, mimetype="text/plain")


mongo = PyMongo(app)
