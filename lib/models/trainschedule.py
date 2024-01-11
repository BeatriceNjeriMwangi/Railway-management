from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import relationship 
import sqlalchemy.orm
from .base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

class TrainSchedule(Base):
    __tablename__ = 'train_schedule'
    id = Column(Integer, primary_key=True)
    arrival_time = Column(String)
    depature_time = Column(String)
    train_id = Column(Integer, ForeignKey("trains.id"))
    station_id = Column(Integer, ForeignKey("stations.id"))

    trains = relationship("Train", back_populates='train_schedule')
    stations = relationship("Station", back_populates='train_schedule')
    def __repr__(self):
        return f"TrainSchedule(id={self.id}, arrival_time={self.arrival_time}, departure_time={self.departure_time}, train_id={self.train_id}, station_id={self.station_id})>"