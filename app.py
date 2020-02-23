from flask import Flask, redirect, render_template, request, session
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


@app.route('/login', methods=["GET", "POST"])
def login():
    error_msg = ""

    if request.method == 'POST':
        mail = request.form.get("mail")
        password = request.form.get("password")

        if (mail and password) and mail == 'user@mail.ru' and password == 'qwe123':
            session["is_auth"] = True
            return redirect('/')
        else:
            error_msg = "Неверное имя или пароль"

    return render_template("auth.html", error_msg=error_msg)


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
