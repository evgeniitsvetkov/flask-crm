from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Работает'


if __name__ == '__main__':
    app.run()
