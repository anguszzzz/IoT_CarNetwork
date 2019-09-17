
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.models.base import  Base
from sqlalchemy import Column, Integer, String,  Boolean
from flask_login import UserMixin #flask login require


class User(Base,UserMixin):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    _password = Column('password', String(128),nullable=False)
    vehicleNumber=Column(Integer,default=0)
    alertNumber=Column(Integer,default=0)




    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password=generate_password_hash(raw)
    def check_password(self,raw):
        if not self._password:
            return False
        return check_password_hash(self._password,raw)
    def is_authenticated(self):
           return True
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))









