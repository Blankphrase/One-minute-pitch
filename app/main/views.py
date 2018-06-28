from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from . import main 
from flask_login import login_required
from .forms import ReviewForm, UpdateProfile
from .. import db
from ..models import Review, User, Category, Pitch

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    category = Category.get_categories()
    title = 'Home - Welcome to The Pitch website'

    return render_template('index.html', title=title, category=category)

@main.route('/category/<int:id>')
def category(id):
    """
    view category function that returns the category and its pitches
    """
    category = Category.query.get(id)
    title = f'{category.name} pitch'
    pitch = Pitch.get_pitches(category.id)

    return render_template('category.html', title=title, category=category, pitch=pitch)


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


@main.route('/category/pitch/new/<int:id>', methods=["GET", "POST"])
@login_required
def new_pitch(id):
    """
    view 
    """
    form = PitchForm()
    category = Category.query.filter_by(id=id).first()
    if form.validate_on_submit():
        username = form.username.data
        post = form.post.data

        new_pitch = Pitch(category_id = category.id, username=username, post=post)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id=category.id))
    title = f'{category.name} pitch'
    return render_template('new_pitch.html', title=title, pitch_form=form, category=category)


@main.route('/pitch/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):

    form = ReviewForm()
    pitch = Pitch.query.filter_by(id=id).first()
    if form.validate_on_submit():
        username=form.username.data
        review = form.review.data

        new_review = Review(pitch_id=pitch.id, username=username, post_review=review)
        new_review.save_review()

        return redirect(url_for('.review', id=pitch.id))

    username = f'{pitch.username} review'
    return render_template('new_review.html', username=username, review_form=form, pitch=pitch)
