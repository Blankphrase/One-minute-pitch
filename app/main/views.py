from flask import Flask, flash, redirect, render_template, request, session, abort
from . import main 

@main.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"


@main.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@main.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
