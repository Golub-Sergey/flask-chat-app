from flask import Flask
from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
socketio = SocketIO(app)
connection = PyMongo(app)
history = connection.db.history