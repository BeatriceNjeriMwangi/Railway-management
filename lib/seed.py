from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models.train import Train
from models.station import Station
from models.trainschedule import TrainSchedule
from models.base import Base

engine = create_engine('sqlite:///Railway.db')
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()


fake = Faker()

def generate_stations():
    for _ in range(5):  # Change 5 to the number of stations you want
        station = Station(
            station_name=fake.word(),
            Location=fake.city()
        )
        session.add(station)

# Function to generate fake data for trains
def generate_trains():
    for _ in range(5):  # Change 5 to the number of trains you want
        train = Train(
            name=fake.word(),
            capacity=fake.random_int(min=100, max=500)
        )
        session.add(train)

# Function to generate fake data for train schedules
def generate_train_schedules():
    stations = session.query(Station).all()
    trains = session.query(Train).all()

    for train in trains:
        for station in stations:
            schedule = TrainSchedule(
                arrival_time=fake.time(),
                depature_time=fake.time(),
                trains=train,
                stations=station
            )
            session.add(schedule)

# Generate data for stations, trains, and train schedules
generate_stations()
generate_trains()
generate_train_schedules()

# Commit the changes to the database
session.commit()