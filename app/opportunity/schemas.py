from marshmallow import fields, Schema
from marshmallow.validate import Length, Range
from .models import OpportunityModel

class OpportunitySchema(Schema):
    opportunity_id = fields.Int()
    title = fields.String()
    stream = fields.String()
    launch_date = fields.DateTime()
    open_date = fields.DateTime()
    close_date = fields.DateTime()

    class Meta:
        model = OpportunityModel
        include_relationships = True
        load_instance = True
        fields = ('opportunity_id', 'title', 'stream', 'launch_date', 'open_date', 'close_date')


# # may not be needed
# class OpportunityRequestSchema(Schema):
#     opportunity_id = fields.Int(required=True)
