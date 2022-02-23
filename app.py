from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import redis

app = Flask(__name__)
api = Api(app)
marshmalow = Marshmallow(app)

app.config.from_object("config.Config")
app.config['SECRET_KEY'] = "59ceec65a970fa3b1a00830e53081eb6f565c272"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

redis_db = redis.Redis(host='redis_container', port=6379, db=1, charset='utf-8', decode_responses=True)

db = SQLAlchemy(app)
db.init_app(app)
db.create_all()

migrate = Migrate(app, db)
migrate.init_app(app, db)


with app.app_context():
    from routes.main import *


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
