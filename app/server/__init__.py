from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
    db.init_app(app)

    from .routes import main

    app.register_blueprint(main, url_prefix='/')


    with app.app_context():
        db.create_all()  

    return app
