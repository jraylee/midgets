from bark_monitor import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello World"

def detect_bark():
    