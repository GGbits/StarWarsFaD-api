from mongoengine import *


class Injury(EmbeddedDocument):
    severity = IntField(min_value=1, max_value=4)
    result = StringField()
