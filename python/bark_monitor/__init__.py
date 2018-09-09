from flask import Flask

app = Flask(__name__)

from bark_monitor import routes
