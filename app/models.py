from app import db


class User(db.Document):
    id = db.StringField()

    wood = db.IntField(required=False, default=0)
    stone = db.IntField(required=False, default=0)
    flint = db.IntField(required=False, default=0)
    hatchets = db.IntField(required=False, default=0)
    weeds = db.IntField(required=False, default=0)
    furs = db.IntField(required=False, default=0)
    knives = db.IntField(required=False, default=0)

    wander = db.BoolField(required=False, default=False)
    get_wood = db.BoolField(required=False, default=False)
    explore = db.BoolField(required=False, default=False)
    get_stone = db.BoolField(required=False, default=False)
    get_flint = db.BoolField(required=False, default=False)
    get_fire = db.BoolField(required=False, default=False)
    get_apples = db.BoolField(required=False, default=False)
