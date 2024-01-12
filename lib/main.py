import click
from models.train import Train
from models.station import Station
from models.trainschedule import TrainSchedule
# from sqlalchemy.orm import sessionmaker



trains = Train()

@click.group()
def train() :
    pass

@click.command()

@click.option('--name',prompt="Enter name",help="name of the train",required=True)
@click.option('--capacity',prompt="Enter capacity",help="capacity of the train",required=True)

def add_train(name,capacity):
    trains.add_train(name,capacity)
    click.echo('successfully added train')

@click.command()
@click.option('--name',prompt="Enter name",help="name of the train",required=True)
def get_name(name):
    train=trains.get_name(name)
    click.echo(f'found  train by the name :{name}')

@click.command()

@click.option('--name',prompt="Enter name",help="name of the train",required=True)
@click.option('--new-capacity',prompt="Enter new capacity",type=int,help="capacity of the train",required=True)
def update(name,new_capacity):
    result = trains.update_train(name, new_capacity)
    click.echo(result)


@click.command()
def list_trains():
    all_trains = trains.list_all_trains()
    for train in all_trains:
        return all_trains
    
@click.command()
@click.option('--name',prompt="Enter name",help="name of the train to delete",required=True)
def delete_train(name):
    trains.delete_train(name)
    # result = trains.delete_train( name)
    # click.echo(result)



                                


stations = Station()



    

@click.command()
@click.option()
def add_station(station_name, Location):
    adding = stations.added_station(station_name, Location)


train.add_command(add_train)
train.add_command(get_name)
train.add_command(update)
train.add_command(list_trains)
train.add_command(delete_train)
train.add_command(add_station)

if __name__ == '__main__':
    
    train()    
    