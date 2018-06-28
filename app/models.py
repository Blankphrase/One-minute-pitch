from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer, primary_key=True)
    username =db.Column(db.String(255), index = True)
    post = db.Column(db.String(400), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    review = db.relationship('Review', backref='pitch', lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitch = Pitch.query.filter_by(category_id=id).all()
        return pitch


class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    post_review = db.Column(db.String(400), index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

    def save_review(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_reviews(cls, id):
        review = Review.query.filter_by(pitch_id=id).all()
        return review

class User(UserMixin, db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch =  db.relationship('Pitch', backref = 'user', lazy = "dynamic")
    review = db.relationship('Review', backref = 'user', lazy = "dynamic")


    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    pitch = db.relationship('Pitch', backref='category', lazy="dynamic")

    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories
