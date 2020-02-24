from flask import Flask, redirect, render_template, request, session
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView

from config import Config
from models import db, User, MyUserView, Group, Applicant

app = Flask(__name__)
app.config.from_object(Config)


class DashboardView(AdminIndexView):

    @expose('/')
    def index(self):
        return self.render('admin/admin_dashboard.html')


admin = Admin(app, index_view=DashboardView())

admin.add_view(MyUserView(User, db.session))
admin.add_view(ModelView(Group, db.session))
admin.add_view(ModelView(Applicant, db.session))


@app.route('/')
def index():
    if not session.get('is_auth'):
        return redirect('/login')

    return '<a href="/admin">Панель администратора</a>'


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


@app.route('/logout', methods=["POST"])
def logout():
    if session.get("is_auth"):
        session.pop("is_auth")
    return redirect("/login")


@app.errorhandler(404)
def render_not_found():
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим:\n{}".format(error.original_exception), 500


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
