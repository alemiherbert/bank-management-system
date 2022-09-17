from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config:
    SECRET_KEY = environ.get("SECRET_KEY") or "a_hard_to_guess_string"
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI") or \
        f"sqlite:///{path.join(basedir, 'database.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
