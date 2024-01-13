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
    
    def get_station(self, name):
        station= session.query(Station).filter(Station.station_name==name).first()
        print (f"found Station {station.station_name} located at {station.Location} ")
    def list_all_stations(self):
      
        all_stations = session.query(Station).all()
        for station in all_stations:
            print(f"Station ID: {station.id}, Name: {station.station_name}, Location: {station.Location}")

      
        return all_stations
        
    def added_station(self, station_name, location):
        new_station = Station(station_name=station_name, Location=location)
        session.add(new_station)
        session.commit()
       

    
    def delete_station(self,name):
        # Retrieve the station to delete
        station_to_delete = session.query(Station).filter(Station.station_name == name).first()

        if station_to_delete:
            # Delete the station
            session.delete(station_to_delete)
            session.commit()
            return print(f"Station {name} deleted successfully")

        else:
            return print(f"Station {name} not found")