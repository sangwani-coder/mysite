#!/usr/bin/env python3
""" Entr point"""
from flask import Flask, render_template
from zyambo.views import app_views
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.register_blueprint(app_views)
app.config["CACHE_TYPE"] = "null"

# Create in-memory database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db.sqlite'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = 'zyambossecret'


# Create models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    github_url = db.Column(db.String(244), unique=False)
    hosted_url = db.Column(db.String(244), unique=False)
    description = db.Column(db.String(244), unique=False)
    date = db.Column(db.DateTime)


class MyContact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    mobile1 = db.Column(db.String(80), unique=True)
    mobile2 = db.Column(db.String(80), unique=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    # Required for administrative interface
    def __unicode__(self):
        return self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    user = db.relationship(User, backref='posts')

    def __unicode__(self):
        return self.title
    
@app.errorhandler(404)
def PageNotFound(error: str) -> str:
    """ Page not found error"""
    return render_template('error.html', error=error), 404

@app.errorhandler(405)
def methodNotAllowed(error: str) -> str:
    """ unauthorized error"""
    return render_template('error.html', error=error), 405


admin = Admin(app, name='Zyambo admin', template_mode='bootstrap4')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Project, db.session))
admin.add_view(ModelView(MyContact, db.session))


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    # Create DB
    with app.app_context():
        db.create_all()

    app.run(debug=False, host='0.0.0.0')
