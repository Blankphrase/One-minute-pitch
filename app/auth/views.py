from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from ..models import User
from .forms import RegistrationForm
from . import auth
from .. import db


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html', registration_form=form)

@auth.route('/login', methods=["GET", "POST"])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return render_template('auth/login.html')


@auth.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('auth/login.html')
