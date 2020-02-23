from flask import Flask, render_template, session
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from config import Config
from models import db, User, MyUserView, Group, Applicant

app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app)

admin.add_view(MyUserView(User, db.session))
admin.add_view(ModelView(Group, db.session))
admin.add_view(ModelView(Applicant, db.session))


@app.route('/')
def index():
    return 'Главная страница'


@app.route('/admin')
def admin():
    return render_template('/admin/admin_dashboard.html')


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
