from mongoengine import *
from Characteristics import Characteristics


class Talent(EmbeddedDocument):
    title = StringField()
    description = StringField()


class Species(Document):
    name = StringField(unique=True)
    characteristics = EmbeddedDocumentField(Characteristics)
    special = StringField()
    talents = EmbeddedDocumentListField(Talent)
    xp = IntField()
    wound = PointField()
    strain = PointField()



