import os

from flask import Flask, url_for, jsonify, request, redirect, current_app, make_response, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from flask.ext.assets import Environment, Bundle
import wtforms as wtf

app = Flask(__name__)
heroku = Heroku(app)

app.config.from_envvar('APP_CONFIG')

# Set up the database
db = SQLAlchemy(app)

# CSS/JS/etc assets
assets = Environment(app)
assets.url = 'static'

assets.register('js_all',
        'js/lib/*.js', 'js/*.js',
        filters='uglifyjs', output='gen/js_all.min.js')

assets.register('css_all',
        'css/*.css',        
        Bundle('css/*.less', filters='less'),
        filters='cssmin',
        output='gen/css_all.min.css')

# Sample Model
class SampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=False)

    def __init__(self, name=''):
        self.name = name

    def __repr__(self):
        return '<SampleModel %r>' % self.name

# Sample forms
class SampleForm(wtf.Form):
    input = wtf.TextField('input', [
        wtf.validators.Required()
        ])

# Sample main page
@app.route('/')
def home():
    return render_template('main.html', page="main")

# Sample setup script
@app.route('/setup/')
def setup():
    sm = SampleModel(name='hi')
    db.session.add(sm)
    db.session.commit()

    return "It worked!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

