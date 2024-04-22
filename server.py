from flask import Flask, render_template
from flask_socketio import SocketIO
import threading

import DB

app = Flask(__name__)
socketio = SocketIO(app)

def fetch_measurements():
    db = DB.connectToDB()
    collection = db["measurement"]
    
    while True:
        measurements = list(collection.find({}, {"_id": 0}))
        socketio.emit("Update_measurements", measurements)
        
        socketio.sleep(1)

# Start the background thread to continuously fetch distances
fetch_thread = threading.Thread(target=fetch_measurements, daemon=True)
fetch_thread.start()

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    print("Client connected")

if __name__ == "__main__":
    socketio.run(app, debug=True)