from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()


class User(db.Model):
    __tablenames__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    mail = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


class MyUserView(ModelView):
    column_exclude_list = ['password']


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default='набирается')
    course = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)


class Applicant(db.Model):
    __tablename__ = 'applicants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    mail = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default='новая')
