from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# class Pitch(db.Model):
#     __tablename__ = 'pitch'

#     id = db.Column(db.Integer, primary_key=True)
#     username =db.Column(db.String(255), index = True)
#     post = db.Column(db.String(400), index=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
#     review = db.relationship('Review', backref='pitch', lazy="dynamic")

#     def save_pitch(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_pitches(cls, id):
#         pitch = Pitch.query.filter_by(category_id=id).all()
#         return pitch


# class Review(db.Model):
#     __tablename__ = 'review'

#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(255), index = True)
#     post_review = db.Column(db.String(400), index = True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

#     def save_review(self):
#         db.session.add(self)
#         db.session.commit()
#     @classmethod
#     def get_reviews(cls, id):
#         review = Review.query.filter_by(pitch_id=id).all()
#         return review

class User(UserMixin, db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    interview = db.relationship('Interview', backref='user', lazy='dynamic')
    advertisement = db.relationship('Advertisement', backref='user', lazy='dynamic')
    project = db.relationship('Project', backref='user', lazy='dynamic')
    music = db.relationship('Music', backref='user', lazy='dynamic')
    seduction = db.relationship('Seduction', backref='user', lazy='dynamic')
    sale = db.relationship('Sale', backref='user', lazy='dynamic')
    general = db.relationship('General', backref='user', lazy='dynamic')
    reviewinterview = db.relationship('ReviewInterview', backref='user', lazy='dynamic')
    reviewadvertisement = db.relationship('ReviewAdvertisement', backref='user', lazy='dynamic')
    reviewproject = db.relationship('ReviewProject', backref='user', lazy='dynamic')
    reviewmusic = db.relationship('ReviewMusic', backref='user', lazy='dynamic')
    reviewseduction = db.relationship('ReviewSeduction', backref='user', lazy='dynamic')
    reviewsale = db.relationship('ReviewSale', backref='user', lazy='dynamic')
    reviewgeneral = db.relationship('ReviewGeneral', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote', backref='user', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='user', lazy='dynamic')


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


class Seduction(db.Model):
    __tablename__ = 'seduction'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_seduction(self):
       db.session.add(self)
       db.session.commit()

class ReviewSeduction(db.Model):
    __tablename__ = 'reviewseduction'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    seduction_id = db.Column(db.Integer, db.ForeignKey('seduction.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_reviewseduction(self):
        db.session.add(self)
        db.session.commit()


class Sale(db.Model):
    __tablename__ = 'sale'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_sale(self):
       db.session.add(self)
       db.session.commit()

class ReviewSale(db.Model):
    __tablename__ = 'reviewsale'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_reviewsale(self):
        db.session.add(self)
        db.session.commit()


class General(db.Model):
    __tablename__ = 'general'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_general(self):
       db.session.add(self)
       db.session.commit()

class ReviewGeneral(db.Model):
    __tablename__ = 'reviewgeneral'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    general_id = db.Column(db.Integer, db.ForeignKey('general.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_reviewgeneral(self):
        db.session.add(self)
        db.session.commit()


class Music(db.Model):
    __tablename__ = 'music'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_music(self):
        db.session.add(self)
        db.session.commit()


class ReviewMusic(db.Model):
    __tablename__ = 'reviewmusic'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    music_id = db.Column(db.Integer, db.ForeignKey("music.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_reviewmusic(self):
        db.session.add(self)
        db.session.commit()


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    review = db.relationship('ReviewProject', backref='project', lazy='dynamic')

    def save_project(self):
        db.session.add(self)
        db.session.commit()


class ReviewProject(db.Model):
    __tablename__ = 'reviewproject'
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(255))
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_reviewproject(self):
        db.session.add(self)
        db.session.commit()


class Advertisement(db.Model):
    __tablename__ = 'advertisement'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_advertisement(self):
        db.session.add(self)
        db.session.commit()


class ReviewAdvertisement(db.Model):
    __tablename__ = 'reviewadvertisement'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    production_id = db.Column(db.Integer, db.ForeignKey("advertisement.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_reviewadvertisement(self):
        db.session.add(self)
        db.session.commit()


class Interview(db.Model):
    __tablename__ = 'interview'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(255))
    body = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_production(self):
        db.session.add(self)
        db.session.commit()


class ReviewInterview(db.Model):
    __tablename__ = 'reviewinterview'
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(255))
    interview_id = db.Column(db.Integer, db.ForeignKey("interview.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_reviewinterview(self):
        db.session.add(self)
        db.session.commit()


class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_upvote(self):
        db.session.add(self)
        db.session.commit()


class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key=True)
    downvote = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_downvote(self):
        db.session.add(self)
        db.session.commit()