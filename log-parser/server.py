from flask import Flask
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/os')
def getOs():
    file = open("data/client_os.json")
    return json.load(file)

@app.route('/ip')
def getIp():
    file = open("data/client_ip.json")
    return json.load(file)

@app.route('/browser')
def getBrowser():
    file = open("data/client_browser.json")
    return json.load(file)

@app.route('/date')
def getDate():
    file = open("data/client_date.json")
    return json.load(file)

@app.route("/geolocation")
def getGeoData():
    file = open("geoData.json")
    return json.load(file)


if __name__ == '__main__':
    app.run(debug=True)  
   