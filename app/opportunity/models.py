from ..db import db
from sqlalchemy.dialects.postgresql import JSON


class OpportunityModel(db.Model):
    __tablename__ = 'opportunity'
    opportunity_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    stream = db.Column(db.String, nullable=False)
    launch_date = db.Column(db.DateTime, nullable=False)
    open_date = db.Column(db.DateTime, nullable=False)
    close_date = db.Column(db.DateTime, nullable=False)
    grant_connect_go_id = db.Column(db.Integer)
    mrff_initiative = db.Column(db.Integer)

    # , grant_connect_go_id, mrff_initiative
    def __init__(self, title, stream, launch_date, open_date, close_date):
        self.title = title
        self.stream = stream
        self.launch_date = launch_date
        self.open_date = open_date
        self.close_date = close_date
        # self.grant_connect_go_id = grant_connect_go_id
        # self.mrff_initiative = mrff_initiative

    def __repr__(self):
        return f"<Opportunity {self.name}>"

