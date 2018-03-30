from app import app
from flask import render_template, request
from models import Users
from forms import LoginForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        item = Users.query.filter_by(usr_name=form.name.data).first()
        return 'User: %s' % item.usr_name
    return render_template('login.html', form=form)


@app.route('/user/<usr_id>')
def usr_show(usr_id):
    return render_template('user.html', item=Users.query.filter_by(usr_id=usr_id).first())
