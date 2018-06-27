from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from . import main 
from flask_login import login_required

@main.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)

@main.route('/pitch/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):
    pass
