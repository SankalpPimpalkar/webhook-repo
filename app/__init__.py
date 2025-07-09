from flask import Flask, send_from_directory
from app.extensions import dbconnect,mongo
from flask_cors import CORS
import os

# Creating our flask app
def create_app():

    app = Flask(__name__, static_folder='dist/assets', template_folder='dist')
    # Configuration
    CORS(app=app)

    # Database connection
    dbconnect(app=app)

    print("STATIC FOLDER:", app.static_folder)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        print("SERVING")
        full_path = os.path.join(app.static_folder, path)
        if path and os.path.exists(full_path):
            return send_from_directory(app.static_folder, path)
        return send_from_directory(app.template_folder, 'index.html')
    
    # registering all the blueprints
    from app.webhook.routes import webhook
    app.register_blueprint(webhook)
    
    return app
