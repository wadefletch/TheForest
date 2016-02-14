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

    Wander = db.BoolField(required=False, default=True)
    Get_Wood = db.BoolField(required=False, default=False)
    Explore = db.BoolField(required=False, default=False)
    Find_Stone = db.BoolField(required=False, default=False)
    Find_Flint = db.BoolField(required=False, default=False)
    Start_Fire = db.BoolField(required=False, default=False)
    Harvest_Apples = db.BoolField(required=False, default=False)

    events = db.ListField(db.StringField(), required=False)

    def log_event(self, event):
        self.events = event + self.events
