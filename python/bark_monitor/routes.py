import json
import os
import numpy as np
from time import time
from flask import make_response, render_template, send_from_directory

from bark_monitor import app

n = 5
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", data="test")

@app.route("/live-data")
def live_data():
    times = np.arange(n) * 1000/n
    times += time() * 1000
    data = np.random.random(n)*100
    package_data = list(zip([list(times), list(data)]))
    response = make_response(json.dumps(package_data))
    response.content_type = "application/json"
    print(package_data)
    return response


@app.route('/js/<path:filename>')
def serve_static(filename):
    root_dir = os.path.join(os.path.dirname(__file__), "../..")

    print(root_dir)
    return send_from_directory(os.path.join(root_dir, 'static', 'js'), filename)