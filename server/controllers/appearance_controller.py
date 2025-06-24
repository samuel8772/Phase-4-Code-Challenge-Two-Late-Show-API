from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.extensions import db
from server.models.appearance import Appearance
from server.models.episode import Episode
from server.models.guest import Guest

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    # Check JSON structure
    if not data or not all(k in data for k in ["rating", "guest_id", "episode_id"]):
        return {"error": "Missing required fields"}, 422
    
    try:
        rating = int(data["rating"])
        guest_id = int(data["guest_id"])
        episode_id = int(data["episode_id"])
    except ValueError:
        return {"error": "Invalid data types"}, 422

    if not (1 <= rating <= 5):
        return {"error": "Rating must be 1-5"}, 422
    
    appearance = Appearance(
        rating=rating,
        guest_id=guest_id,
        episode_id=episode_id
    )
    db.session.add(appearance)
    db.session.commit()
    
    return {
        "id": appearance.id,
        "rating": appearance.rating,
        "guest_id": appearance.guest_id,
        "episode_id": appearance.episode_id
    }, 201