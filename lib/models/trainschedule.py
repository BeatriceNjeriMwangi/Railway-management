from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import relationship 
import sqlalchemy.orm
from .base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Railway.db')


Session = sessionmaker(bind=engine)
session = Session()

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
        return f"TrainSchedule(id={self.id}, arrival_time={self.arrival_time}, depature_time={self.depature_time}, train_id={self.train_id}, station_id={self.station_id})>"
    def add_to_schedule(self,train_id, station_id, depature_time,arrival_time):
        new_schedule = TrainSchedule(
            train_id=train_id,
            station_id=station_id,
            depature_time=depature_time,
            arrival_time=arrival_time
        )
        session.add(new_schedule)
        session.commit()
        return print(f"Schedule added for train {train_id} at station {station_id}")
        
    
    def list_schedule(self):
        all_schedules = session.query(TrainSchedule).all()
        return print(all_schedules)
    
    def delete_schedule(self,schedule_id):
        deleted_schedule = session.query(TrainSchedule).filter_by(id=schedule_id).first()

        if deleted_schedule:
            session.delete(deleted_schedule)
            session.commit()
            return print(f"Schedule {schedule_id} deleted successfully")
        else:
            return print(f"Schedule with ID {schedule_id} not found")