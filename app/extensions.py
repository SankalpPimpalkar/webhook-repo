from flask_pymongo import PyMongo

# Setup MongoDB here
mongo = PyMongo(uri="mongodb+srv://test:sp5tfHCtdC7Nd6OW@test.pcwr8.mongodb.net/?retryWrites=true&w=majority&appName=test")
db = mongo.github_webhooks
collection = db.events