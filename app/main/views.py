from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from . import main 
from flask_login import login_required
from .forms import ReviewForm, UpdateProfile
from .. import db
from ..models import Review, User

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    title = 'Home - Welcome to The Pitch website'

    return render_template('index.html', title=title)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/pitch/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):

    form = ReviewForm()

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # new_review = Review(pitch.id, title, pitch.poster, review)
        # new_review.save_review()

        # return redirect(url_for('.movie', id=pi.id))

    # title = f'{movie.title} review'
    return render_template('new_review.html', review_form=form)
