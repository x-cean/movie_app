from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# define association table first above user and movie classes
user_movies = db.Table(
    'user_movies',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
)


# define user class
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    # relationship attribute, not sure whether back ref is necessary in this case
    movies = db.relationship('Movie', secondary='user_movies', backref='users')

    def __repr__(self):
        return f"User(id: {self.id}, name: {self.name})"

    def __str__(self):
        return f"User(id: {self.id}, name: {self.name})"


# define movie class
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    director = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    def __repr__(self):
        return (f"Movie(id: {self.id}, name: {self.name}, "
                f"director: {self.director}, year: {self.year})")

    def __str__(self):
        return (f"Movie(id: {self.id}, name: {self.name}, "
                f"director: {self.director}, year: {self.year})")






