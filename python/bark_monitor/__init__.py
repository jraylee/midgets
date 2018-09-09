from flask import Flask
import os

root_dir = os.path.join(os.path.dirname(__file__), "../..")
templates_dir = os.path.join(root_dir, "templates")
static_dir = os.path.join(root_dir, "static")

app = Flask(__name__, template_folder=templates_dir, static_folder=root_dir)

from bark_monitor import routes
