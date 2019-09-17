from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import  Base
from app.models.user import User


class Vehicles(Base):
    __tablename__ = 'Vehicles'

    id=Column(Integer,primary_key=True,autoincrement= True)
    uid=Column(Integer,ForeignKey('User.id'))
    vehiclePlate=Column(String(50),nullable=False,unique=True)
    apiKey=Column(String(100),nullable=False,unique=True)
    brand=Column(String(20))
    registerDate=Column(String(40))
    email = Column(String(50),nullable=False)
    type=Column(String(20))
    location=Column(String(50))
    speed=Column(Float(50))
    acceleration=Column(Float(20))
    videos=Column(String(1000))
    image=Column(String(50))
    videoNumber=Column(Integer,default=0)


    def Gennerate_apiKey(self, vehiclePlate):
        self.apiKey = generate_password_hash(vehiclePlate)

    def check_apiKey(self, vehiclePlate):
        if not self.apiKey:
            return False
        return check_password_hash(self.apiKey, vehiclePlate)