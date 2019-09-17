from flask import Flask

from app.models.base import db

from flask_login  import LoginManager



login_manager = LoginManager()

def create_app():
    app=Flask(__name__)
    register_blueprint(app)
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')

    login_manager.init_app(app)
    login_manager.login_view ='web.login'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

def register_blueprint(app):
    from app.web.tfl import web
    from app.web.location import web
    from app.web.user import web
    from app.web.vehicles import web
    from app.web.recording import web
    from app.web.Chart import web
    from app.web.video import web
    from app.web.alert import web

    app.register_blueprint(web)
