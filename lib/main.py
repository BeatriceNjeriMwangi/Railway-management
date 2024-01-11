import click
from models.train import Train
from models.station import Station
from models.trainschedule import TrainSchedule

trains = Train()

@click.group()
def train() :
    pass

@click.command()

@click.option('--name',prompt="Enter name",help="name of the train",required=True)
@click.option('--capacity',prompt="Enter capacity",help="capacity of the train",required=True)

def add(name,capacity):
    trains.add_train(name,capacity)
    click.echo('successfully added train')


@click.command()
@click.option('--name',prompt="Enter name",help="name of the train",required=True)
def get_name(name):
    train=trains.get_name(name)
    click.echo(f'found  train by the name :{name}')

# @click.command()

# @click.option('--name',prompt="Enter name",help="name of the train",required=True)
# @click.option('--capacity',prompt="Enter capacity",help="capacity of the train",required=True)
# def update(name,capacity):
#     train = trains.update_train(capacity)
#     click.echo(train)
                                
train.add_command(add)
train.add_command(get_name)
# train.add_command(update)
if __name__ == '__main__':
    train()    
