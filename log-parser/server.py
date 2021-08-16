from os import system
from flask import Flask
from flask_cors import CORS
import index 

app = Flask(__name__)
CORS(app)

# global variables 
clients=[]
browsers=[]
dates=[]
systems=[]

def main():
    log_file= open("access.log")
    
    for line in log_file:
        ip = index.client_ip(line)
        browser= index.browser_used(line)
        date = index.date_time(line)
        os = index.os_type(line)
        if ip: clients.append(ip[0])
        if browser: browsers.append(browser[0])
        if date: dates.append(date[0])
        if os: systems.append(os[0])
 
    print(dict(index.count(clients)))
    print(dict(index.count(browsers)))
    print(dict(index.count(dates)))
    print(dict(index.count(systems)))
    log_file.close()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/os')
def getOs():
    return  dict(index.count(systems))

@app.route('/ip')
def getIp():
    return  dict(index.count(clients))

@app.route('/browser')
def getBrowser():
    return  dict(index.count(browsers))

@app.route('/date')
def getDate():
    return  dict(index.count(dates))


if __name__ == '__main__':
    main()  
    app.run(debug=True)  
   