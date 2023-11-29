# ----------<__INIT__.PY>------------------------------------------------------------------------------------#

# Importing necessary libraries and modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


#p.printProccess("<__init__>: Starting")
# Define the database name and its URI
DB_NAME = "liteDB_cita450.db"
DataBase = f"sqlite:///{DB_NAME}"

# Initialize the SQLAlchemy database instance
db = SQLAlchemy()

# ----------<FUNCTIONS>------------------------------------------------------------------------------------#

# Function to create and configure the Flask application
def create_app():
    # Create a Flask app instance
    app = Flask(__name__)

    # Configuring secret key and database URI for the application
    app.config["SECRET_KEY"] = "passmypasstopass"
    app.config["SQLALCHEMY_DATABASE_URI"] = DataBase

    # Initialize the database with the app
    db.init_app(app)

    # Importing blueprints for different parts of the application
    from .auth import auth, authAdmin
    from .views import views, public

    # Registering blueprints with their respective URL prefixes
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(public, url_prefix="/public/")
    app.register_blueprint(authAdmin, url_prefix="/admin/")

    # Importing the User model
    from .models import User

    # Create database tables within the application context, if they don't exist
    with app.app_context():
        db.create_all()
 #       p.printProccess(f"<__init__>: Database @{DataBase} validated")
      
    # Setting up the login manager for user session management
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # User loader callback for Flask-Login to load a user from the User ID stored in the session
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

# ----------<END>------------------------------------------------------------------------------------#