import csv
import uuid
from mongoengine import *
from settings import DBNAME
from Species import *

connect(DBNAME)


# TODO: create another csv for species talents, import that first, then using the name, relate talents to species
def import_species(file):
    with open(file) as f:
        data =[tuple(line) for line in csv.reader(f)]

    tuple_list = []
    for tup in data:
        tuple_list.append(Species(
            id=uuid.uuid4(),
            name=tup[0],
            characteristics=Characteristics(
                brawn=tup[1],
                agility=tup[2],
                intellect=tup[3],
                cunning=tup[4],
                willpower=tup[5],
                presnce=tup[6]
                ),
            special=tup[7],
            talents=Talent(
                title=tup[8],
                description=tup[9]
                ),
            xp=tup[10],
            wound=tup[11],
            strain=tup[12]
            ))

    for species in tuple_list:
        species.save()


import_species("import/species.csv")
