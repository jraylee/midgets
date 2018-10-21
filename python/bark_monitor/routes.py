import json
import os
import numpy as np
from time import time
from flask import make_response, render_template, send_from_directory
from my_midgets.bark_midget import BarkMidget
from bark_monitor import app

bark_midget = BarkMidget()
bark_midget.start()

n = 1
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", data="test")

@app.route("/live-data")
def live_data():
    data = [time() * 1000, max(list(bark_midget.frames)[-100:])]
    response = make_response(json.dumps(data))
    response.content_type = "application/json"
    print(data)
    return response

@app.route('/js/<path:filename>')
def serve_static(filename):
    root_dir = os.path.join(os.path.dirname(__file__), "../..")

    print(root_dir)
    return send_from_directory(os.path.join(root_dir, 'static', 'js'), filename)