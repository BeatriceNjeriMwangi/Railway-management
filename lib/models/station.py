from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import relationship 
import sqlalchemy.orm
from .base import Base, session
from sqlalchemy.ext.declarative import declarative_base

class Station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True)
    station_name = Column(String)
    Location = Column(String)

    train_schedule = relationship("TrainSchedule", back_populates="stations") 


    def __repr__(self):
        return f"Station(id={self.id}, station_name={self.station_name},location={self.location})>"