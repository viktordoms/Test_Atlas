from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


app = Flask(__name__)
api = Api(app)
marshmalow = Marshmallow(app)

app.config.from_object("config.Config")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
db.init_app(app)
db.create_all()

migrate = Migrate(app, db)
migrate.init_app(app, db)


with app.app_context():
    from routes.main import *


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
