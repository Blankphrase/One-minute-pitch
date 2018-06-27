from flask import render_template
from . import auth

@auth.route('/login', methods=['POST'])
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
