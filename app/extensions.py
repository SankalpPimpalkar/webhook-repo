from flask_pymongo import PyMongo

# Setup MongoDB here
mongo = PyMongo()

def dbconnect(app):

    app.config["MONGO_URI"] = "mongodb+srv://test:sp5tfHCtdC7Nd6OW@test.pcwr8.mongodb.net/github_webhooks"
    mongo.init_app(app=app)

    print("Mongo Info", mongo.db)