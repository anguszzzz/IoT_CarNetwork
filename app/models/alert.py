

from sqlalchemy import Column, Integer, ForeignKey, String

from app.models.base import Base


class Alert(Base):
    id = Column(Integer, primary_key=True)
    message=Column(String(100))
    userid = Column(Integer, ForeignKey('User.id'))
    Plate=Column(String(50),ForeignKey('Vehicles.vehiclePlate'))