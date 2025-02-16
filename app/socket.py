# app/socket.py
from flask_socketio import SocketIO, emit
import os

# configure cors_allowed_origins
if os.environ.get('FLASK_ENV') == 'production':
    origins = [
        'https://elya-le-banter.onrender.com',  # <-- your render URL
        'http://elya-le-banter.onrender.com'
    ]
else:
    origins = "*"

# initialize your socket instance
socketio = SocketIO(cors_allowed_origins=origins)

# handle chat messages
@socketio.on("chat")
def handle_chat(data):
    print("Received chat message:", data)  # <-- log received message
    emit("chat", data, broadcast=True)
    print("Broadcasting chat message:", data)  # <-- log broadcasting message)
