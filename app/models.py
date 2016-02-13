from app import db


class User(db.Document):
    cookie = db.StringField()

    wood = db.IntField()
    stone = db.IntField()
    flint = db.IntField()
    hatchets = db.IntField()
    plant_material = db.IntField()
    furs = db.IntField()
    knives = db.IntField()

    wander = db.BoolField()
    get_wood = db.BoolField()
    explore = db.BoolField()
    get_stone = db.BoolField()
    get_flint = db.BoolField()
    get_fire = db.BoolField()
    get_apples = db.BoolField()
