from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import relationship 
import sqlalchemy.orm
from .base import Base, session
from sqlalchemy.ext.declarative import declarative_base

class Train(Base):
    __tablename__ = 'trains'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capacity = Column(Integer)
    train_schedule = relationship("TrainSchedule", back_populates="trains") 

    def __repr__(self):
        return f"<Train(id={self.id}, name={self.name}, capacity={self.capacity})>"

