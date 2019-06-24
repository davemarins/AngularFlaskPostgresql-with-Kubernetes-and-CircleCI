# -*- coding: utf-8 -*-
"""Default api blueprints for Demo application."""

from flask import Blueprint, jsonify

route = Blueprint('default', __name__)

@route.route("/")
def main_page():
    return "<p>Hello to GCP</p>"

@route.route("/api")
def hello():
    return "Hello from Flask using Python 3.7.3!!"

@route.route("/api/ping")
def ping():
    return jsonify({"status": 200, "msg":"This message is coming from Flask backend!"})