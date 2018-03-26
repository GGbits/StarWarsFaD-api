from mongoengine import *

# Variables
CHARACTERISTICS = ["brawn", "agility", "intellect", "cunning", "willpower", "presence"]


# Class
class Characteristics(EmbeddedDocument):
    brawn = IntField(min_value=1, max_value=6)
    agility = IntField(min_value=1, max_value=6)
    intellect = IntField(min_value=1, max_value=6)
    cunning = IntField(min_value=1, max_value=6)
    willpower = IntField(min_value=1, max_value=6)
    presence = IntField(min_value=1, max_value=6)
