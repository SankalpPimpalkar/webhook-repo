from flask import Blueprint, jsonify, request
import datetime
import uuid
from app.extensions import mongo

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    payload = request.json
    event_type = request.headers.get('X-GitHub-Event')
    collection = mongo.db.get_collection(name='events')

    # Schema for mongodb document to track events
    doc = {
        "request_id": str(uuid.uuid4()),
        "author": None,
        "action": None,
        "from_branch": None,
        "to_branch": None,
        "timestamp": datetime.utcnow()
    }

    if event_type == "push":
        doc["author"] = payload["pusher"]["name"]
        doc["action"] = "push"
        doc["from_branch"] = payload["ref"].split("/")[-1]
        doc["to_branch"] = payload["ref"].split("/")[-1]

    elif event_type == "pull_request":
        pr = payload["pull_request"]
        doc["author"] = pr["user"]["login"]
        doc["from_branch"] = pr["head"]["ref"]
        doc["to_branch"] = pr["base"]["ref"]

        if payload["action"] == "opened":
            doc["action"] = "pull_request_opened"
        elif payload["action"] == "closed" and pr.get("merged", False):
            doc["action"] = "pull_request_merged"
        else:
            return jsonify({
                "success": False,
                "message": "Unhandled pull_request action"
            }), 400
    else:
        return jsonify({"message": "Event ignored"}), 200

    # Saving event to collection
    collection.insert_one(doc)

    return jsonify({
        "success": True,
        "message": f"{event_type} event is added"
    }), 201

@webhook.route('/events', methods=["GET"])
def get_events():
    action = request.args.get('action')
    print(mongo.db)
    collection = mongo.db.get_collection(name='events')

    query = { "action": action } if action else {} 
    # I added an extra feature for filtering events based on actions

    events = list(collection.find(query, {'_id': 0}))

    return jsonify({
        "success": True,
        "message": "Successfully fetch events",
        "payload": events
    })