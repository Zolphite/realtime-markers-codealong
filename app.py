# from types import MethodDescriptorType
# from typing import Text
from flask import Flask, render_template, request
from flask_cors import CORS
import requests
import os

from flask_socketio import SocketIO, emit

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
cors = CORS(app, resources={r"/api/*" : {"orgins": "*"}})

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

@app.route('/api/back_end', methods=['GET', 'POST'])
def back_end():
    return 'Hello'

# SocketIO Functions
clickMarkers = {}
idLinks = {}

@socketio.on('connect')
def client_connect():
    emit('on_connect', 'Connected')
    emit('update_markers', clickMarkers)

@socketio.on('disconnect')
def client_disconnect():
    if request.sid in idLinks:
        print('disconnected with marker')
        del clickMarkers[idLinks[request.sid]]
        emit('remove_marker', idLinks[request.sid], broadcast=True)

@socketio.on('on_click')
def on_click(sendList):
    # print(request.sid)
    clickMarkers[sendList[0]] = sendList[1]
    idLinks[request.sid] = sendList[0]
    emit('update_markers', clickMarkers, broadcast=True)

if __name__ == "__main__":
    print("server is running on localhost!!")
    socketio.run(app, port=5000)