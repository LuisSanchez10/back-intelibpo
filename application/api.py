from flask import Blueprint
from flask_restful import Api
from application.controller import CallsTopics, CallsHours, Calls_R

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

api.add_resource(CallsTopics, '/api/topics-char')
api.add_resource(CallsHours, '/api/hours-bar')
api.add_resource(Calls_R, '/api/add-call')