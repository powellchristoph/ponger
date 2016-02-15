from flask import Flask
from flask_restful import Resource, Api

__author__ = 'Chris Powell <powellchristoph@gmail.com>'

app = Flask(__name__)
api = Api(app)

class PongerAPI(Resource):
    def get(self):
        return {'message': 'pong'}

api.add_resource(PongerAPI, '/ping')

if __name__ == '__main__':
    app.run()
