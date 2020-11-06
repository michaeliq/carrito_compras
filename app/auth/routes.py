from flask import render_template, redirect, url_for, request, abort
from flask_login import login_user, login_required, logout_user
from . import auth
from .forms import UserForm, SignUpForm
from app.models import User

@auth.route('/auth/login/',methods=['POST','GET'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.password == form.password.data:
            login_user(user)
            print('login success')
            next = request.args.get('next')
            if next is not None:
                return redirect(next)

            return redirect(url_for('sell.home'))
        else:
            print('email o clave incorrecta')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html',form=form)

@auth.route('/auth/signup/',methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User(email=email,password=password)
        User.save(user)
        return redirect(url_for('sell.home'))
    return render_template('auth/signup.html',form=form)

@auth.route('/auth/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('sell.home'))


