from flask_restful import Resource
from api.quotes import quotes


class Quotes(Resource):
    def get(self):
        return quotes
