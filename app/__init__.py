from flask import Flask, jsonify
from app.extensions import dbconnect,mongo
from flask_cors import CORS

# Creating our flask app
def create_app():

    app = Flask(__name__)
    # Configuration
    CORS(app=app)

    # Database connection
    dbconnect(app=app)

    @app.route('/', methods=['GET'])
    def home():
        print(mongo.db)
        return jsonify({
            "success": True,
            "message": "App is running",
            "payload": {
                "mongodb": mongo.db.name,
            }
        })
    
    # registering all the blueprints
    from app.webhook.routes import webhook
    app.register_blueprint(webhook)
    
    return app
