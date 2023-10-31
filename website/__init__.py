# ----------<__INIT__.PY>------------------------------------------------------------------------------------#
#
#
#
# ----------<IMPORTS>------------------------------------------------------------------------------------#
print("__init__: Starting")
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
#
# ----------<INSTANCE>------------------------------------------------------------------------------------#
print("__init__: Creating db variables")
DB_NAME = "liteDB_cita450.db"
DataBase = f"sqlite:///{DB_NAME}"
global db
db = SQLAlchemy()
#
#
# ----------<FUNCTIONS>------------------------------------------------------------------------------------#
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "passmypasstopass"
    app.config["SQLALCHEMY_DATABASE_URI"] = DataBase
    db.init_app(app)
    from .auth import auth, authAdmin
    from .views import views, public

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(public, url_prefix="/public/")
    app.register_blueprint(authAdmin, url_prefix="/admin/")
    from .models import User, Portfolio, Note, Ledger, Admin

    with app.app_context():
        db.create_all()
        print(f"__init__: Check/Create db = {DataBase}")
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
#
#
# ----------<END>------------------------------------------------------------------------------------#
