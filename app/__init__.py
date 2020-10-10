from flask import Flask, request, jsonify, make_response

from app.config import Config

# Init app
app = Flask(__name__)
app.config.from_object(Config)


from app import views