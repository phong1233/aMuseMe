from flask import Flask
from services import Services

app = Flask(__name__)

services = Services()

@app.route("/")
def home():
    return "Hello, hello!"

@app.route("/pause", methods=['GET'])
def pause():
    return services.pause_song()


    
if __name__ == "__main__":
    app.run(debug=True)