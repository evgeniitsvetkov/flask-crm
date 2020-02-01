from flask import Flask, render_template, session
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from config import Config
from models import db, User, Group, Applicant

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
admin = Admin(app)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Group, db.session))
admin.add_view(ModelView(Applicant, db.session))


@app.route('/')
def index():
    return 'Работает'


if __name__ == '__main__':
    app.run()
