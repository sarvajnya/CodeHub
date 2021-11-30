from flask import Flask
from config import Config_info
from flask_mongoengine import MongoEngine
from application.compiler_path import compiler_path
# from flask_restplus import Api


# api = Api()

app = Flask(__name__)
app.config.from_object(Config_info)

db = MongoEngine()
db.init_app(app)
compiler_path_object = compiler_path()
compiler_path_object.fetch_path()
# api.init_app(app)

from application import routes

if __name__ == '__main__':
    app.run()

