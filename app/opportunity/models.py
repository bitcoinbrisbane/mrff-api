from ..db import db


class OpportunityModel(db.Model):
    __tablename__ = 'opportunity'
    opportunity_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    stream = db.Column(db.String, nullable=False)
    launch_date = db.Column(db.DateTime, nullable=False)
    open_date = db.Column(db.DateTime, nullable=False)
    close_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, opportunity_id, title, stream, launch_date, open_date, close_date):
        self.opportunity_id = opportunity_id
        self.title = title
        self.stream = stream
        self.launch_date = launch_date
        self.open_date = open_date
        self.close_date = close_date
        

    def __repr__(self):
        return {
            'id': self.opportunity_id, 
            'title': self.title, 
            'stream': self.stream, 
            'launch_date': self.launch_date,
            'open_date': self.open_date,
            'close_date': self.close_date
        }

