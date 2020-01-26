from flask import Flask
from services import Services

app = Flask(__name__)

services = Services()

@app.route("/")
def home():
    return "Hello, hello!"

@app.route("/pause", methods=['POST'])
def pause():
    return services.pause_song()
@app.route("/play", methods=['POST'])
def play():
    return services.play_song()
@app.route("/unpause", methods=['POST'])
def unpause():
    return services.unpause.song()
@app.route("/stop", methods=['POST'])
def stop():
    return services.stop_song()
@app.route("/status", methods=['GET'])
def status():
    return services.status_song()

if __name__ == "__main__":
    app.run(debug=True)