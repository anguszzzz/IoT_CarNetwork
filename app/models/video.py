from sqlalchemy import Column, String, ForeignKey, Integer

from app.models.base import Base


class Video(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    path=Column(String(100),unique=True)
    carPlate = Column(String(50), ForeignKey('Vehicles.vehiclePlate'))
    uploadDate = Column(String(40))
    videoName=Column(String(50),unique=True)
    uid = Column(Integer, ForeignKey('User.id'))