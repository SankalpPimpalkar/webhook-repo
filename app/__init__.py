from flask import Flask
from extensions import mongo
from app.webhook.routes import webhook


# Creating our flask app
def create_app():

    app = Flask(__name__)

    # Configurations
    app.config["MONGO_URI"] = "mongodb+srv://test:sp5tfHCtdC7Nd6OW@test.pcwr8.mongodb.net/?retryWrites=true&w=majority&appName=test"
    mongo.init_app(app=app)

    @app.route('/', methods=['GET'])
    def home():
        return "App is running"
    
    # registering all the blueprints
    app.register_blueprint(webhook)
    
    return app
