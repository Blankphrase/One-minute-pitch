from flask import Flask, flash, redirect, render_template, request, session, abort
from . import main 
from flask_login import login_required

@main.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"


@main.route('/pitch/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):
    pass
