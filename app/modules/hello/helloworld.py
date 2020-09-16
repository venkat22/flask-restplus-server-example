from flask import Flask
from flask_restplus._http import HTTPStatus

from app.extensions.api import Namespace
from flask_restplus_patched import Resource

api = Namespace('hello', description="Hello World")
@api.route('/',methods=['GET'])
class Hello(Resource):

    @api.response(
        code=HTTPStatus.NOT_FOUND,
        description="Team or member not found.",
    )
    def get(self):
        return "Hello World!"



