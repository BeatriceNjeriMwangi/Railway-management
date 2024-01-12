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
        return f"Station(id={self.id}, station_name={self.station_name},Location={self.Location})>"
    
    def get_station(station_name):
        return session.query(Station).filter_by(Station.station_name==station_name).first()
    
    def list_all_stations():
        all_stations = session.query(Station).all()
        return all_stations
    def added_station(self, station_name, Location):
        new_station = Station(station_name=station_name, Location=Location)
        session.add(new_station)
        session.commit()
       

    def update_station(self, station_name, new_station_name):
        updated_station = session.query(Station).filter(station_name == new_station_name).first()
        if updated_station:
            updated_station.name=new_station_name
            session.commit()
            return(f"Station{station_name} updated")
        
        else:
            return(f"Station{station_name} not updated")

    def delete_station(station_name):
        deleted_station = session.query(Station).filter(Station.station_name==station_name)

        if deleted_station:
            session.delete(deleted_station)
            session.commit()
            return(f"Station{station_name} has been deleted")
        else:
            return(f"Station{station_name} not deleted")