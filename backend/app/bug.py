from flask import Blueprint, request, jsonify
from flask_login import current_user

from app.extensions import db
from app.models.bug import Bug

bp = Blueprint('bugs', __name__, url_prefix='/bugs')


@bp.route('/', methods=["GET", "POST"])
def get_bugs():
    if request.method == 'GET':
        bugs = [{'id': bug.id, 'title': bug.title, 'description': bug.description} for bug in current_user.bugs]
        return jsonify({'bugs': bugs})
    else:
        title = request.json['title']
        description = request.json['description']
        new_bug = Bug(title=title, description=description)
        db.session.add(new_bug)
        db.session.commit()
        return jsonify({'message': 'Bug created'}), 201


@bp.route('/<int:bug_id>', methods=["GET"])
def get_appeal(bug_id):
    bug = Bug.query.filter_by(id=bug_id).first()

    if bug is None:
        return jsonify({'error': 'Bug not found'})

    return jsonify({'id': bug.id, 'title': bug.title, 'description': bug.description}), 200
