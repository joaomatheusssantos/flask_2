from flask import Flask
from sqlalchemy import Boolean
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
import jwt
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
CORS(app)


app.config['SECRET_KEY'] = 'Matheus2'
jwt = JWTManager(app) 


host = app.config["FLASK_HOST"]
port = app.config["FLASK_PORT"]


server = Server(host=host, port=port)
manager.add_command("runserver", server)
manager.add_command("db", MigrateCommand)


from app.models.role_models import Role
from app.models.user_models import User
from app.models.action_models import Action
from app.models.resource_models import Resource
from app.models.privilege_models import Privilege
from app.models.controller_models import Controller


from app.controllers import user_controller
from app.controllers import role_controller
from app.controllers import resource_controller
from app.controllers import action_controller
from app.controllers import privilege_controller
from app.controllers import controller_controller
from app.controllers import auth_controller
