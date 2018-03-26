from mongoengine import *
from Characteristics import *

# Variables
CATEGORY = ["general", "combat", "knowledge"]
EMO_STRENGTH = []
EMO_WEAKNESS = []


# Interior classes
class Defense(EmbeddedDocument):
    ranged = IntField()
    melee = IntField()


class HealthStat(EmbeddedDocument):
    current = IntField()
    threshold = IntField()


# Exterior Classes
class Attributes(EmbeddedDocument):
    soak = IntField()
    wounds = EmbeddedDocumentField(HealthStat)
    strain = EmbeddedDocumentField(HealthStat)
    defense = EmbeddedDocumentField(Defense)


class Description(EmbeddedDocument):
    gender = StringField(choices=["Male", "Female"])
    age = IntField(min_value=1, max_value=1000)
    height = IntField(min_value=36, max_value=1000)
    build = StringField()
    hair = StringField()
    eyes = StringField()
    features = StringField()


class Morality(EmbeddedDocument):
    emo_strength = StringField(choices=EMO_STRENGTH)
    emo_weakness = StringField(choices=EMO_WEAKNESS)
    conflict = IntField(min_value=0, max_value=10)
    morality = IntField(min_value=0, max_value=100)


class Skill(EmbeddedDocument):
    name = StringField()
    category = StringField(choices=CATEGORY)
    characteristic = StringField(choices=CHARACTERISTICS)
    career = BooleanField()
    rank = IntField(min_value=0, max_value=5)


class Xp(EmbeddedDocument):
    total_xp = IntField(min_value=0)
    available_xp = IntField(min_value=0)


# Player Class
class Player(Document):
    # TODO: Finish filling out Skills
    id = UUIDField()
    c_id = UUIDField()
    name = StringField()
    description = EmbeddedDocument(Description)
    species = UUIDField()
    career = UUIDField()
    specializations = ListField(UUIDField())
    force_rating = IntField(min_value=0, max_value=5) # TODO: Is this is real min\max?
    attributes = EmbeddedDocumentField(Attributes)
    characteristics = EmbeddedDocumentField(Characteristics)
    skills = EmbeddedDocumentListField(Skill)
    weapons = ListField(UUIDField())
    xp = EmbeddedDocument(Xp)
    motivations = ListField(UUIDField())
    morality = EmbeddedDocument(Morality)
    equipment = ListField(UUIDField())
    credits = IntField()
    injuries = UUIDField()
    talents = ListField(UUIDField())
    force_powers = ListField(UUIDField)