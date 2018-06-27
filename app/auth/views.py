from flask import Flask, flash, redirect, render_template, request, session, abort
from . import auth


@auth.route('/login', methods=['POST', 'GET'])
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
