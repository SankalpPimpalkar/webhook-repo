from flask_pymongo import PyMongo

# Setup MongoDB here
mongo = PyMongo()
db = mongo.github_webhooks
collection = db.events