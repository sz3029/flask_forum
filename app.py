from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from routes import *
app.config['SECRET_KEY'] = 'ABC12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
