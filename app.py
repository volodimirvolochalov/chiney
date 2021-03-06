from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

if __name__ == '__main__':
    app.run()