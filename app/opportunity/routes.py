from flask import current_app, Blueprint, abort, jsonify, request, Response
from ..db import db
from .models import OpportunityModel
from .schemas import OpportunitySchema

opportunity = Blueprint('opportunity', __name__)
opportunity_schema = OpportunitySchema()

# get all opportunities max 100
@opportunity.route('/', methods=['GET'], strict_slashes=False)
def get():
    max = 100
    if 'max' in request.args:
        max = int(request.args.get('max'))

    query = OpportunityModel.query.order_by(OpportunityModel.id.desc()).limit(max)
    result = opportunity_schema.dump(query, many=True)
    return jsonify(result)


# get opportunity by id
@opportunity.route('/<int:id>', methods=['GET'], strict_slashes=False)
def get_by_id(id):
    opportunity = OpportunityModel.query.get(id)
    if opportunity is None:
        abort(404)

    result = opportunity_schema.dump(opportunity)
    return jsonify(result)

