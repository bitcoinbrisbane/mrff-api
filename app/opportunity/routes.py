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

    # order_by(OpportunityModel.opportunity_id.desc()).limit(max)
    query = OpportunityModel.query.all()
    result = opportunity_schema.dump(query, many=True)
    return jsonify(result)


@opportunity.route('/', methods=['POST'], strict_slashes=False)
def post():
    data = request.get_json()
    if not data:
        abort(400)

    print(data)
    # opportunity = opportunity_schema.load(data)
    opportunity = OpportunityModel(request.json['title'], request.json['stream'],
                                   request.json['launch_date'], request.json['open_date'], request.json['close_date'])
    db.session.add(opportunity)
    db.session.commit()
    result = opportunity_schema.dump(opportunity)
    return jsonify(result), 201


# get opportunity by id
@opportunity.route('/<int:id>', methods=['GET'], strict_slashes=False)
def get_by_id(id):
    opportunity = OpportunityModel.query.get(id)
    if opportunity is None:
        abort(404)

    result = opportunity_schema.dump(opportunity)
    return jsonify(result)
