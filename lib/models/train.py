from typing import Any
from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import relationship 
import sqlalchemy.orm
from .base import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Railway.db')


Session = sessionmaker(bind=engine)
session = Session()
all_trains=[]
class Train(Base):
    __tablename__ = 'trains'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capacity = Column(Integer)
    train_schedule = relationship("TrainSchedule", back_populates="trains") 

    def __repr__(self):
        return f"<Train(id={self.id}, name={self.name}, capacity={self.capacity})>"

    def add_train(self, name, capacity):
        new_train = Train(name=name, capacity=capacity)
        session.add(new_train)
        session.commit()

    def get_name(self,name):
        return session.query(Train).filter_by(name = name).first()
        
        
    def update_train(self,name, new_capacity):
       
        update= session.query(Train).filter(Train.name == name).first()
        if update:
            
            update.capacity=new_capacity
            session.commit()
            return f"Train {name} updated successfully."
        else:
            return f"Train with name {name} not found."
        
        #list all trains
    def list_all_trains(self):
        all_trains=session.query(Train).all()
        return all_trains
    
    #deleting a train
    def delete_train(name):
        train_delete = session.query(Train).filter(Train.name==name).first()
        if train_delete:
            session.delete(train_delete)
            session.commit()
            return (f"Train by {name}is deleted")
        else:
            return (f"Train by {name}is not found")

