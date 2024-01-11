from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import relationship 
import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker
from .base import Base
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Railway.db')


Session = sessionmaker(bind=engine)
session = Session()

class Station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True)
    station_name = Column(String)
    Location = Column(String)

    train_schedule = relationship("TrainSchedule", back_populates="stations") 


    def __repr__(self):
        return f"Station(id={self.id}, station_name={self.station_name},location={self.location})>"