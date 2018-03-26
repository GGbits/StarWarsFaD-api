from mongoengine import *
from Characteristics import *


class Talent(EmbeddedDocument):
    title = StringField()
    description = StringField()


class Species(Document):
    id = UUIDField
    name = StringField()
    characteristics = EmbeddedDocument(Characteristics)
    special = StringField()
    talents = EmbeddedDocumentListField(Talent)
    xp = IntField()
    wound = PointField()
    strain = PointField()



