from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.train import Train
from models.station import Station
from models.trainschedule import TrainSchedule
from models.base import Base


engine = create_engine('sqlite:///Railway.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()


train=Train()
train1=Train(name="beta", capacity=80)
train.add_train(train1.name, train1.capacity)

train=Train()
train.get_name()
