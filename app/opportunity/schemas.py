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
        fields = ('height', 'hash', 'timestamp', 'fee', 'size') 


# may not be needed
class OpportunityRequestSchema(Schema):
    opportunity_id = fields.Int(required=True)
