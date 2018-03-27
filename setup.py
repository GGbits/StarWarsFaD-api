import json
from mongoengine import *
from settings import DBNAME
from Species import Species, Talent
from Characteristics import Characteristics

connect(DBNAME)


# TODO: create another csv for species talents, import that first, then using the name, relate talents to species
def import_species(file):
    species_json = json.load(open(file))
    for s in species_json:
        species_object = Species(
            name=s['name'],
            characteristics=Characteristics(
                brawn=s['characteristics']['brawn'],
                agility=s['characteristics']['agility'],
                intellect=s['characteristics']['intellect'],
                cunning=s['characteristics']['cunning'],
                willpower=s['characteristics']['willpower'],
                presence=s['characteristics']['presence']
            ),
            special=s['special'],
            talents=[Talent(title=t['title'], description=t['description']) for t in s['talents']],
            xp=s['xp'],
            wound=s['wound'],
            strain=s['strain']
        )
        species_object.save()


if __name__ == '__main__':
    import_species("import/species.json")
